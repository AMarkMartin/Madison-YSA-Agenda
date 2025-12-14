#!/usr/bin/env python3
"""
Madison YSA Agenda Update Script

This script automates the weekly update process for the Madison YSA agenda.
Simply edit the configuration below and run this script to generate the updated index.html.

Usage:
    python update_agenda.py
"""

from datetime import datetime

# ============================================================================
# CONFIGURATION - Edit this section to update the agenda
# ============================================================================

# Week date (displayed at the top)
WEEK_DATE = "December 14, 2025"

# Inspirational Quote
QUOTE = {
    "text": "I am the light of the world: he that followeth me shall not walk in darkness, but shall have the light of life.",
    "citation": "John 8:12"
}

# Optional image URL (leave empty string for placeholder)
IMAGE_URL = "images/calling_the_fishermen.jpeg"

# Agenda Items - Each item has a title and description
AGENDA_ITEMS = [
    {
        "title": "Conducting",
        "description": "Grant"
    },
    {
        "title": "Presiding",
        "description": ""
    },
    {
        "title": "Announcements",
        "description": "Tithing Declaration: Talk to Daniel or see QR code below<br>" +
                        " <br>" + ""
                        " <br>" + ""
                        " <br>" + ""
                        " <br>" + ""
                        ""
    },
    {
        "title": "Opening Hymn",
        "description": "209 Hark! The Herald Angels Sing"
    },
    {
        "title": "Opening Prayer",
        "description": "Amy Rich"
    },
    {
        "title": "Ward Business",
        "description": ""
    },
    {
        "title": "Stake Business",
        "description": ""
    },
    {
        "title": "Sacrament Hymn",
        "description": "178 O Lord of Hosts"
    },
    {
        "title": "Sacrament",
        "description": "Administration of the Sacrament"
    },
    {
        "title": "Speaker",
        "description": "Katie Gaertner, 1st councilor in the Stake YW Presidency"
    },
    {
        "title": "Intermediate Hymn",
        "description": "212 Far, Far Away on Judea’s Plains"
    },
    {
        "title": "Speaker",
        "description": "Connie Mathison, Stake RS President"
    },
    {
        "title": "Closing Hymn",
        "description": "201 Joy to the World"
    },
    {
        "title": "Closing Prayer",
        "description": "Emily Lym"
    }
]

# Announcements
ANNOUNCEMENTS = [
    "Institute classes continue Wednesday evenings at 7:30 PM"
]

# Resources - Each resource has an icon (emoji), text, and URL
RESOURCES = [
    {
        "icon": "⛪",
        "text": "Ward Website",
        "url": "https://local.churchofjesuschrist.org/en/units/us/wi/madison-ysa-ward"
    },
    {
        "icon": "💻",
        "text": "Ward Discord",
        "url": "https://discord.gg/KychmWchBc"
    },
    {
        "icon": "🗣️",
        "text": "Ward Facebook",
        "url": "https://www.facebook.com/groups/8627328790/"
    },
    {
        "icon": "📖",
        "text": "Church Website",
        "url": "https://www.churchofjesuschrist.org"
    },
    {
        "icon": "📚",
        "text": "Scriptures",
        "url": "https://www.churchofjesuschrist.org/study/scriptures"
    },
    {
        "icon": "🎵",
        "text": "Hymns & Music",
        "url": "https://www.churchofjesuschrist.org/music"
    },
    {
        "icon": "⛪",
        "text": "Temples",
        "url": "https://www.churchofjesuschrist.org/temples"
    },
    {
        "icon": "📅",
        "text": "Church Calendar",
        "url": "https://www.churchofjesuschrist.org/calendar"
    },
    {
        "icon": "📚",
        "text": "Participate in Ward Music",
        "url": "https://docs.google.com/forms/d/e/1FAIpQLSeoICCUoUSlmm_jvNJ6oiN9djGkn0XKiVsZZJM55yRK2Rrong/viewform?usp=sharing&ouid=109596045431617318151"
    },
    {
        "icon": "📚",
        "text": "Sign up for a Musical Number",
        "url": "https://docs.google.com/forms/d/e/1FAIpQLSevEiFzwyJOWaN2MZiyMsc9mQVddy-1vz8zTaLPRg_BQIkmZw/viewform?usp=header"
    },
    {
        "icon": "💬",
        "text": "Meeting with Bishop Clinton",
        "url": "https://calendly.com/ysamadison/15min?back=1&month=2024-04"
    }
]

# ============================================================================
# HTML GENERATION - Don't edit below this line unless you know what you're doing
# ============================================================================

def generate_inspiration_section():
    """Generate the inspiration section HTML."""
    if IMAGE_URL:
        image_html = f'<img src="{IMAGE_URL}" alt="Inspirational image">'
    else:
        image_html = '<div class="placeholder-image"></div>'
    
    return f'''        <section class="inspiration">
            <div class="inspiration-image">
                {image_html}
            </div>
            <div class="inspiration-quote">
                <blockquote>
                    <p>"{QUOTE['text']}"</p>
                    <cite>— {QUOTE['citation']}</cite>
                </blockquote>
            </div>
        </section>'''

def generate_agenda_items():
    """Generate the agenda items HTML."""
    items_html = []
    for item in AGENDA_ITEMS:
        items_html.append(f'''            <div class="agenda-item">
                <div class="details">
                    <strong>{item['title']}</strong>
                    <p>{item['description']}</p>
                </div>
            </div>''')
    return '\n\n'.join(items_html)

def generate_announcements():
    """Generate the announcements HTML."""
    announcements_html = []
    for announcement in ANNOUNCEMENTS:
        announcements_html.append(f'                <li>{announcement}</li>')
    return '\n'.join(announcements_html)

def generate_resources():
    """Generate the resources HTML."""
    resources_html = []
    for resource in RESOURCES:
        resources_html.append(f'''                <a href="{resource['url']}" target="_blank" class="resource-link">
                    <span class="link-icon">{resource['icon']}</span>
                    <span class="link-text">{resource['text']}</span>
                </a>''')
    return '\n'.join(resources_html)

def generate_html():
    """Generate the complete HTML file."""
    # Get today's date for the footer
    today = datetime.now().strftime("%B %d, %Y")
    
    html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Madison YSA - Weekly Agenda</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>Madison YSA</h1>
            <h2>Sacrament Meeting Agenda</h2>
            <p class="date">Week of {WEEK_DATE}</p>
        </header>

        <main>
{generate_inspiration_section()}

            <section class="agenda">
                <h3>Today's Agenda</h3>
                
{generate_agenda_items()}
            </section>

            <section class="announcements">
                <h3>Announcements</h3>
                <ul>
{generate_announcements()}
                </ul>
            </section>

            <section class="resources">
                <h3>Resources & Links</h3>
                <div class="resource-links">
{generate_resources()}
                </div>
            </section>
        </main>

        <footer>
            <p>Madison Young Single Adult Ward</p>
            <p class="update-info">Last updated: {today}</p>
        </footer>
    </div>
</body>
</html>
'''
    return html_template

def main():
    """Main function to generate and save the HTML file."""
    print("Generating updated index.html...")
    
    # Generate the HTML
    html_content = generate_html()
    
    # Write to index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✓ Successfully updated index.html")
    print(f"✓ Week: {WEEK_DATE}")
    print(f"✓ Agenda items: {len(AGENDA_ITEMS)}")
    print(f"✓ Announcements: {len(ANNOUNCEMENTS)}")
    print(f"✓ Resources: {len(RESOURCES)}")
    print("\nNext steps:")
    print("1. Review the updated index.html file")
    print("2. Commit and push your changes:")
    print("   git add index.html")
    print(f"   git commit -m 'Update agenda for week of {WEEK_DATE}'")
    print("   git push")

if __name__ == "__main__":
    main()
