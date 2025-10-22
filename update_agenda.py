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
WEEK_DATE = "October 22, 2025"

# Inspirational Quote
QUOTE = {
    "text": "I am the light of the world: he that followeth me shall not walk in darkness, but shall have the light of life.",
    "citation": "John 8:12"
}

# Optional image URL (leave empty string for placeholder)
IMAGE_URL = ""

# Agenda Items - Each item has a title and description
AGENDA_ITEMS = [
    {
        "title": "Opening Hymn",
        "description": "Hymn #2 - \"The Spirit of God\""
    },
    {
        "title": "Invocation",
        "description": "Brother Smith"
    },
    {
        "title": "Ward Business",
        "description": "Announcements and upcoming events"
    },
    {
        "title": "Sacrament Hymn",
        "description": "Hymn #169 - \"As Now We Take the Sacrament\""
    },
    {
        "title": "Sacrament",
        "description": "Administration of the Sacrament"
    },
    {
        "title": "Speaker",
        "description": "Sister Johnson - \"Faith in Jesus Christ\""
    },
    {
        "title": "Musical Number",
        "description": "Sister Anderson - \"I Know That My Redeemer Lives\""
    },
    {
        "title": "Speaker",
        "description": "Brother Williams - \"Gratitude and Service\""
    },
    {
        "title": "Closing Hymn",
        "description": "Hymn #220 - \"Lord, We Ask Thee Ere We Part\""
    },
    {
        "title": "Benediction",
        "description": "Sister Davis"
    }
]

# Announcements
ANNOUNCEMENTS = [
    "Youth Conference - November 15-17",
    "Service Project - This Saturday at 9:00 AM",
    "Institute classes continue Wednesday evenings at 7:00 PM"
]

# Resources - Each resource has an icon (emoji), text, and URL
RESOURCES = [
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
        "icon": "💬",
        "text": "Get Help & Support",
        "url": "https://www.churchofjesuschrist.org/get-help"
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
