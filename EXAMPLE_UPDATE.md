# Example: Updating the Agenda Using the Python Script

This example shows how easy it is to update the agenda using `update_agenda.py`.

## Scenario: Preparing for Next Week (October 29, 2025)

### Step 1: Open `update_agenda.py`

Open the file in any text editor (VS Code, Notepad, nano, etc.)

### Step 2: Edit the Configuration Section

Find the configuration section (starts at line 11) and make your changes:

```python
# Week date (displayed at the top)
WEEK_DATE = "October 29, 2025"  # ← Changed from October 22

# Inspirational Quote
QUOTE = {
    "text": "Be strong and of a good courage; be not afraid, neither be thou dismayed.",  # ← New quote
    "citation": "Joshua 1:9"  # ← New citation
}
```

### Step 3: Update Agenda Items

You can easily modify, add, or remove items:

```python
AGENDA_ITEMS = [
    {
        "title": "Opening Hymn",
        "description": "Hymn #27 - \"Praise to the Man\""  # ← Changed hymn
    },
    {
        "title": "Invocation",
        "description": "Brother Lee"  # ← Changed person
    },
    # ... keep other items ...
    {
        "title": "Speaker",
        "description": "Brother Thompson - \"The Power of Prayer\""  # ← New speaker
    },
    # Add a new item by adding another dictionary:
    {
        "title": "Youth Speakers",
        "description": "Emma and Jacob - \"Our Testimonies\""  # ← New item!
    },
    # ... rest of items ...
]
```

### Step 4: Update Announcements

Add, remove, or modify announcements easily:

```python
ANNOUNCEMENTS = [
    "Temple Trip - Next Friday at 6:00 AM (meet at chapel)",  # ← New announcement
    "Youth Conference - November 15-17 - Sign up today!",      # ← Modified
    "Game Night - This Friday at 7:00 PM at the Jones' home",  # ← New announcement
    "Institute classes continue Wednesday evenings at 7:00 PM"
]
```

### Step 5: (Optional) Add a Custom Image

```python
# Optional image URL (leave empty string for placeholder)
IMAGE_URL = "https://example.com/your-image.jpg"  # ← Add your image URL
```

### Step 6: Run the Script

```bash
python update_agenda.py
```

You'll see output like:
```
Generating updated index.html...
✓ Successfully updated index.html
✓ Week: October 29, 2025
✓ Agenda items: 11
✓ Announcements: 4
✓ Resources: 6

Next steps:
1. Review the updated index.html file
2. Commit and push your changes:
   git add index.html
   git commit -m 'Update agenda for week of October 29, 2025'
   git push
```

### Step 7: Commit and Push

```bash
git add index.html update_agenda.py
git commit -m "Update agenda for week of October 29, 2025"
git push
```

## Benefits Over Manual Editing

### Before (Manual HTML Editing):
- Navigate through 150+ lines of HTML
- Find each section individually
- Risk breaking HTML structure with typos
- Hard to add new items without copying/pasting HTML

### After (Python Script):
- All editable content in one place (lines 11-103)
- Clear structure with labeled sections
- Can't break HTML structure
- Easy to add items - just add a new dictionary!

## Tips

### Adding Multiple Speakers
```python
AGENDA_ITEMS = [
    # ... other items ...
    {
        "title": "Speaker",
        "description": "Sister Martinez - \"Charity Never Faileth\""
    },
    {
        "title": "Speaker",  # Same title, different person
        "description": "Brother Chen - \"Following the Savior\""
    },
    {
        "title": "Speaker",  # You can have as many as needed
        "description": "Sister Brown - \"Missionary Work\""
    },
    # ... more items ...
]
```

### Removing an Item
Just delete the entire dictionary block or comment it out:
```python
AGENDA_ITEMS = [
    # This item is removed by commenting it out:
    # {
    #     "title": "Musical Number",
    #     "description": "Sister Anderson"
    # },
    {
        "title": "Speaker",
        "description": "Brother Williams"
    },
]
```

### Custom Resources
```python
RESOURCES = [
    # Add your ward-specific resources:
    {
        "icon": "🏠",
        "text": "Ward Website",
        "url": "https://your-ward-website.com"
    },
    {
        "icon": "📧",
        "text": "Ward Email",
        "url": "mailto:ward@example.com"
    },
    # Keep or remove default resources as needed
]
```

## Quick Reference

All you need to edit is in the CONFIGURATION section (lines 11-103):
- `WEEK_DATE`: The week to display
- `QUOTE`: Inspirational quote with citation
- `IMAGE_URL`: Optional image (or leave empty)
- `AGENDA_ITEMS`: List of agenda items (title + description)
- `ANNOUNCEMENTS`: List of announcements
- `RESOURCES`: List of resource links

That's it! No HTML knowledge required.
