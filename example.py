#!/usr/bin/env python3
"""
pip3 install garth requests readchar

export EMAIL=<your garmin email>
export PASSWORD=<your garmin password>

"""
import datetime
from datetime import timezone
import json
import logging
import os
import sys
from getpass import getpass


import readchar
import requests
from garth.exc import GarthHTTPError

from garminconnect import (
    Garmin,
    GarminConnectAuthenticationError,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
)

# Configure debug logging
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Load environment variables if defined
email = os.getenv("GARMIN_EMAIL")
password = os.getenv("GARMIN_PASSWORD")
tokenstore = os.getenv("GARMIN_TOKEN_STORE") or "~/.garminconnect"
tokenstore_base64 = os.getenv("GARMINTOKENS_BASE64") or "~/.garminconnect_base64"
api = None

# Example selections and settings

# Let's say we want to scrape all activities using switch menu_option "p". We change the values of the below variables, IE startdate days, limit,...
today = datetime.date.today()
startdate = today - datetime.timedelta(days=7)  # Select past week
limit = 100  # Limit the number of activities
start = 0  # Page start

# Filter on activity type, e.g., 'running', 'cycling', 'swimming', etc.
activitytype = ""
activitytype = "running"


def init_api(email, password):
    """Initialize Garmin API with your credentials."""

    try:
        # Using Oauth1 and OAuth2 token files from directory
        print(
            f"Trying to login to Garmin Connect using token data from directory '{tokenstore}'...\n"
        )

        # Using Oauth1 and Oauth2 tokens from base64 encoded string
        # print(
        #     f"Trying to login to Garmin Connect using token data from file '{tokenstore_base64}'...\n"
        # )
        # dir_path = os.path.expanduser(tokenstore_base64)
        # with open(dir_path, "r") as token_file:
        #     tokenstore = token_file.read()

        garmin = Garmin()
        garmin.login(tokenstore)

        print("Login successful!")

        return garmin

    except (FileNotFoundError, GarminConnectAuthenticationError):
        # Session is expired. You'll need to log in again
        print(
            "Login tokens not working, try to login with your credentials...\n"
        )
        try:
            # Ask for credentials if not set as environment variables
            if not email or not password:
                email, password = get_credentials()

            garmin = Garmin(email, password)
            garmin.login()
            # Save Oauth1 and Oauth2 token files to directory for next login
            garmin.garth.dump(tokenstore)
            print(
                f"You can now copy the content of the directory '{tokenstore}' to your application/project.\n"
            )
            print("Login successful!")

            return garmin

        except (FileNotFoundError, GarminConnectAuthenticationError, requests.exceptions.HTTPError) as err:
            logger.error(err)
            return None

    except Exception as err:
        logger.error(err)
        return None


def get_credentials():
    """Get user credentials."""
    
    email = input("Login e-mail: ")
    password = getpass("Enter password: ")
    
    return email, password


def get_menu_choice():
    """Get menu choice from user."""
    
    print("\nSelect option by pressing key:")
    print("(a) Activities")
    print("(l) Last activity")
    print("(s) Stats and body composition")
    print("(h) Heart rate data")
    print("(b) Body battery data")
    print("(t) Training readiness and training status")
    print("(r) Personal records")
    print("(u) User summary")
    print("(d) Download activities")
    print("(p) Scrape all activities")
    print("(q) Quit")
    
    return readchar.readkey()


def print_menu():
    """Print examples menu."""
    print(
        "\n***Garmin Connect API Example***\n"
        "Press 'a' for activities\n"
        "Press 'l' for last activity\n"
        "Press 's' for stats and body composition\n"
        "Press 'h' for heart rate data\n"
        "Press 'b' for body battery data\n"
        "Press 't' for training readiness and training status\n"
        "Press 'r' for personal records\n"
        "Press 'u' for user summary\n"
        "Press 'd' for download activities\n"
        "Press 'p' for scrape all activities\n"
        "Press 'q' to quit\n"
    )


def switch(api, menu_option):
    """Switch between API examples."""
    
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    
    if menu_option == "a":
        # Get activities data for the last 10 activities
        print("\nGetting activities...")
        activities = api.get_activities(0, 10)
        print(json.dumps(activities, indent=4, default=str))
        
    elif menu_option == "l":
        # Get last activity
        print("\nGetting last activity...")
        activities = api.get_activities(0, 1)
        if activities:
            last_activity = activities[0]
            print(json.dumps(last_activity, indent=4, default=str))
        else:
            print("No activities found")
            
    elif menu_option == "s":
        # Get stats and body composition
        print("\nGetting stats and body composition...")
        stats = api.get_stats(current_date)
        body_comp = api.get_body_composition(current_date)
        print("Stats:", json.dumps(stats, indent=4, default=str))
        print("Body composition:", json.dumps(body_comp, indent=4, default=str))
        
    elif menu_option == "h":
        # Get heart rate data
        print("\nGetting heart rate data...")
        hr_data = api.get_heart_rate(current_date)
        print(json.dumps(hr_data, indent=4, default=str))
        
    elif menu_option == "b":
        # Get body battery data
        print("\nGetting body battery data...")
        bb_data = api.get_body_battery(current_date, current_date)
        print(json.dumps(bb_data, indent=4, default=str))
        
    elif menu_option == "t":
        # Get training readiness and training status
        print("\nGetting training readiness and training status...")
        tr_data = api.get_training_readiness(current_date)
        ts_data = api.get_training_status(current_date)
        print("Training readiness:", json.dumps(tr_data, indent=4, default=str))
        print("Training status:", json.dumps(ts_data, indent=4, default=str))
        
    elif menu_option == "r":
        # Get personal records
        print("\nGetting personal records...")
        pr_data = api.get_personal_records()
        print(json.dumps(pr_data, indent=4, default=str))
        
    elif menu_option == "u":
        # Get user summary
        print("\nGetting user summary...")
        summary = api.get_user_summary(current_date)
        print(json.dumps(summary, indent=4, default=str))
        
    elif menu_option == "d":
        # Download activities
        print("\nDownloading activities...")
        activities = api.get_activities(0, 10)
        for activity in activities:
            activity_id = activity['activityId']
            filename = f"activity_{activity_id}.json"
            with open(filename, 'w') as f:
                json.dump(activity, f, indent=4, default=str)
            print(f"Downloaded: {filename}")
            
    elif menu_option == "p":
        # Scrape all activities
        print(f"\nScraping activities from {startdate} to {today}...")
        all_activities = []
        start_idx = 0
        
        while True:
            activities = api.get_activities(start_idx, limit)
            if not activities:
                break
            
            all_activities.extend(activities)
            start_idx += limit
            
            # Check if we've reached the start date
            if activities:
                last_activity_date = datetime.datetime.strptime(
                    activities[-1]['startTimeLocal'][:10], "%Y-%m-%d"
                ).date()
                if last_activity_date < startdate:
                    break
        
        # Filter by date range
        filtered_activities = []
        for activity in all_activities:
            activity_date = datetime.datetime.strptime(
                activity['startTimeLocal'][:10], "%Y-%m-%d"
            ).date()
            if startdate <= activity_date <= today:
                filtered_activities.append(activity)
        
        print(f"Found {len(filtered_activities)} activities")
        
        # Save to file
        filename = f"activities_{startdate}_{today}.json"
        with open(filename, 'w') as f:
            json.dump(filtered_activities, f, indent=4, default=str)
        print(f"Saved to: {filename}")
        
    else:
        print("Invalid option")


def main():
    """Main function."""
    
    # Initialize API
    api = init_api(email, password)
    
    if api:
        print("\n*** Garmin Connect API Example ***")
        
        # Menu loop
        while True:
            print_menu()
            option = get_menu_choice()
            
            if option == "q":
                print("Goodbye!")
                break
            elif option in ["a", "l", "s", "h", "b", "t", "r", "u", "d", "p"]:
                try:
                    switch(api, option)
                except Exception as err:
                    logger.error(f"Error in option '{option}': {err}")
            else:
                print(f"Invalid option: {option}")
    else:
        print("Failed to initialize API")


if __name__ == "__main__":
    main()
