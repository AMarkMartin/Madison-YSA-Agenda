# How to Update the Agenda

**NEW!** You can now use the automated Python script instead of manually editing HTML.

## Option 1: Use the Python Script (Recommended)

The easiest way to update the agenda is using the `update_agenda.py` script:

1. Open `update_agenda.py` in any text editor
2. Edit the configuration section at the top (lines 11-103):
   - Update `WEEK_DATE` 
   - Update `QUOTE` text and citation
   - Modify `AGENDA_ITEMS` - add, remove, or edit items
   - Update `ANNOUNCEMENTS` - add, remove, or edit announcements
   - Update `RESOURCES` if needed
3. Run the script:
   ```bash
   python update_agenda.py
   ```
4. Commit and push your changes:
   ```bash
   git add index.html update_agenda.py
   git commit -m "Update agenda for week of [DATE]"
   git push
   ```

The script will automatically generate the updated `index.html` file with today's date in the footer.

## Option 2: Manual HTML Editing

If you prefer to edit the HTML directly, this guide shows you exactly what to change each week.

## Step 1: Update the Date

Find this line in `index.html` (around line 13):
```html
<p class="date">Week of October 22, 2025</p>
```

Change it to the current week:
```html
<p class="date">Week of October 29, 2025</p>
```

## Step 2: Update the Inspirational Quote

Find the inspiration section (around line 18) and update the quote:
```html
<blockquote>
    <p>"I am the light of the world: he that followeth me shall not walk in darkness, but shall have the light of life."</p>
    <cite>— John 8:12</cite>
</blockquote>
```

Change to a different scripture or quote:
```html
<blockquote>
    <p>"Be strong and of a good courage; be not afraid, neither be thou dismayed."</p>
    <cite>— Joshua 1:9</cite>
</blockquote>
```

## Step 3: (Optional) Add Your Own Image

To add a custom image, replace the placeholder div:
```html
<div class="inspiration-image">
    <div class="placeholder-image"></div>
</div>
```

With an image tag:
```html
<div class="inspiration-image">
    <img src="your-image-url.jpg" alt="Inspirational image">
</div>
```

## Step 4: Update Agenda Items

Each agenda item looks like this (note: no times are shown):
```html
<div class="agenda-item">
    <div class="details">
        <strong>Opening Hymn</strong>
        <p>Hymn #2 - "The Spirit of God"</p>
    </div>
</div>
```

To change the opening hymn, update:
- The hymn number and name: `Hymn #2 - "The Spirit of God"`

## Step 5: Update Speakers

Find speaker sections and update the name and topic:
```html
<div class="agenda-item">
    <div class="details">
        <strong>Speaker</strong>
        <p>Sister Johnson - "Faith in Jesus Christ"</p>
    </div>
</div>
```

Change to:
```html
<div class="agenda-item">
    <div class="details">
        <strong>Speaker</strong>
        <p>Brother Lee - "Service to Others"</p>
    </div>
</div>
```

## Step 6: Update Announcements

Find the announcements section:
```html
<ul>
    <li>Youth Conference - November 15-17</li>
    <li>Service Project - This Saturday at 9:00 AM</li>
    <li>Institute classes continue Wednesday evenings at 7:00 PM</li>
</ul>
```

Add, remove, or modify list items as needed:
```html
<ul>
    <li>Temple Trip - Next Friday at 6:00 AM</li>
    <li>Game Night - This Friday at 7:00 PM</li>
    <li>Institute classes continue Wednesday evenings at 7:00 PM</li>
</ul>
```

## Step 7: Update the Footer Date

Find this line at the bottom (around line 146):
```html
<p class="update-info">Last updated: October 22, 2025</p>
```

Change to today's date:
```html
<p class="update-info">Last updated: October 29, 2025</p>
```

## Step 8: Save and Upload

1. Save the `index.html` file
2. Commit and push to GitHub:
   ```bash
   git add index.html
   git commit -m "Update agenda for week of October 29, 2025"
   git push
   ```

That's it! The website will automatically update on GitHub Pages within a few minutes.

## Tips

- You can add or remove agenda items by copying/pasting the entire `<div class="agenda-item">` block
- Keep the structure intact - only change the text inside
- If you break something, you can always revert using `git checkout index.html`
