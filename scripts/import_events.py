#!/usr/bin/env python3
"""
Google Calendar iCal Import Script

This script fetches calendar events from a Google Calendar's public iCal URL,
parses them using the icalendar library, and outputs them as JSON to data/events.json.

Configuration:
Set GOOGLE_CALENDAR_URL in your .env file with the public iCal URL from Google Calendar.

Usage:
    python import_google_calendar.py
"""

import json
import sys
import os
from datetime import datetime, timezone, date
from pathlib import Path
import requests
from icalendar import Calendar
import pytz
from dotenv import load_dotenv


def get_calendar_url():
    """Get the calendar URL from environment variable."""
    # Load environment variables from .env file
    load_dotenv()

    # Get calendar URL from environment variable
    calendar_url = os.getenv("GOOGLE_CALENDAR_URL")
    if not calendar_url:
        print("Error: GOOGLE_CALENDAR_URL not found in environment variables.")
        print("Please set GOOGLE_CALENDAR_URL in your .env file.")
        print()
        print("To get this URL:")
        print("1. Go to Google Calendar")
        print("2. Click on the calendar name in the left sidebar")
        print("3. Click 'Settings and sharing'")
        print("4. Scroll down to 'Integrate calendar'")
        print("5. Copy the 'Public URL to this calendar (iCal format)'")
        print("6. Add it to your .env file as: GOOGLE_CALENDAR_URL=your_url_here")
        sys.exit(1)

    print(f"Using calendar URL from environment: {calendar_url[:50]}...")
    return calendar_url


def fetch_calendar_data(url):
    """Fetch calendar data from the provided URL."""
    try:
        print(f"Fetching calendar data from: {url}")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching calendar data: {e}")
        sys.exit(1)


def parse_datetime(dt_value, debug_title=None):
    """Parse datetime from icalendar format to ISO string with proper timezone handling."""
    if dt_value is None:
        return None

    # Handle different datetime types
    if hasattr(dt_value, "dt"):
        dt = dt_value.dt
        # Also check if there's timezone parameter info
        params = getattr(dt_value, "params", {})
        tzid = params.get("TZID")
    else:
        dt = dt_value
        tzid = None

    # Check if it's a date object (not datetime)
    if hasattr(dt, "year") and not hasattr(dt, "hour"):
        # It's a date object, convert to datetime at midnight
        dt = datetime.combine(dt, datetime.min.time())
        return dt.isoformat()
    elif hasattr(dt, "hour"):
        # It's a datetime object
        if hasattr(dt, "tzinfo") and dt.tzinfo is not None:
            # Has timezone info - convert UTC times to local time (Europe/Vienna)
            if dt.tzinfo == timezone.utc:
                # This is a UTC time, convert to Europe/Vienna (UTC+2 in summer, UTC+1 in winter)
                vienna_tz = pytz.timezone("Europe/Vienna")
                local_time = dt.astimezone(vienna_tz)
                return local_time.isoformat()
            else:
                # Keep the original timezone
                return dt.isoformat()
        else:
            # No timezone info, assume local time
            return dt.isoformat()
    else:
        # Fallback for other types
        return str(dt)


def filter_future_events(events, max_events=10):
    """Filter events to only include today's and future events, limited to max_events."""
    today = date.today()
    
    # Filter for today and future events
    future_events = []
    for event in events:
        start_str = event.get("start")
        if start_str:
            try:
                # Parse the start date
                start_dt = datetime.fromisoformat(start_str.replace('Z', '+00:00'))
                event_date = start_dt.date()
                
                # Include events from today onwards
                if event_date >= today:
                    future_events.append(event)
            except (ValueError, AttributeError):
                # If we can't parse the date, include the event to be safe
                future_events.append(event)
    
    # Sort by start date and limit to max_events
    future_events.sort(key=lambda x: x.get("start", ""))
    return future_events[:max_events]


def parse_calendar_events(calendar_data):
    """Parse calendar events from iCal data and convert to JSON format."""
    try:
        cal = Calendar.from_ical(calendar_data)
    except Exception as e:
        print(f"Error parsing calendar data: {e}")
        sys.exit(1)

    events = []

    for component in cal.walk():
        if component.name == "VEVENT":
            event = {}

            # Basic event information
            event["id"] = str(component.get("uid", ""))
            event["title"] = str(component.get("summary", ""))
            event["description"] = str(component.get("description", ""))
            event["location"] = str(component.get("location", ""))

            # Dates and times (pass title for debugging)
            event["start"] = parse_datetime(component.get("dtstart"), event["title"])
            event["end"] = parse_datetime(component.get("dtend"), event["title"])
            event["created"] = parse_datetime(component.get("created"))
            event["modified"] = parse_datetime(component.get("last-modified"))

            # Additional properties
            event["status"] = str(component.get("status", "CONFIRMED"))
            event["organizer"] = str(component.get("organizer", ""))

            # Handle recurring events
            rrule = component.get("rrule")
            if rrule:
                event["recurring"] = True
                event["rrule"] = str(rrule)
            else:
                event["recurring"] = False

            # Categories/tags
            categories = component.get("categories")
            if categories:
                if isinstance(categories, list):
                    event["categories"] = [str(cat) for cat in categories]
                else:
                    event["categories"] = [str(categories)]
            else:
                event["categories"] = []

            # URL
            event["url"] = str(component.get("url", ""))

            # All-day event detection
            dtstart = component.get("dtstart")
            if dtstart and hasattr(dtstart, "dt"):
                event["all_day"] = not hasattr(dtstart.dt, "hour")
            else:
                event["all_day"] = False

            events.append(event)

    return events


def save_events_to_json(events, output_path):
    """Save events to JSON file."""
    try:
        # Ensure the data directory exists
        output_path.parent.mkdir(exist_ok=True)

        # Sort events by start date
        events.sort(key=lambda x: x.get("start", ""))

        # Create output data structure
        output_data = {
            "last_updated": datetime.now(timezone.utc).isoformat(),
            "total_events": len(events),
            "events": events,
        }

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

        print(f"Successfully saved {len(events)} events to {output_path}")

    except Exception as e:
        print(f"Error saving events to JSON: {e}")
        sys.exit(1)


def main():
    """Main function."""
    # Get the script directory and calculate paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    output_path = project_root / "data" / "events.json"

    print("Google Calendar to JSON Converter")
    print("=" * 35)

    # Get calendar URL
    calendar_url = get_calendar_url()

    # Fetch calendar data
    calendar_data = fetch_calendar_data(calendar_url)

    # Parse events
    print("Parsing calendar events...")
    events = parse_calendar_events(calendar_data)

    print(f"Found {len(events)} total events")

    # Filter for today's and future events (max 10)
    print("Filtering for today's and future events (max 10)...")
    filtered_events = filter_future_events(events, max_events=10)

    print(f"Keeping {len(filtered_events)} events (today and future, max 10)")

    if not filtered_events:
        print("No current or future events found in the calendar.")
        return

    # Save to JSON
    save_events_to_json(filtered_events, output_path)

    print("\nEvent import completed successfully!")
    print(f"Events saved to: {output_path}")


if __name__ == "__main__":
    main()
