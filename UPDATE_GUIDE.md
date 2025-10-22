# Example: How to Update the Agenda

This guide shows you exactly what to change each week.

## Step 1: Update the Date

Find this line in `index.html` (around line 13):
```html
<p class="date">Week of October 22, 2025</p>
```

Change it to the current week:
```html
<p class="date">Week of October 29, 2025</p>
```

## Step 2: Update Agenda Items

Each agenda item looks like this:
```html
<div class="agenda-item">
    <span class="time">11:00 AM</span>
    <div class="details">
        <strong>Opening Hymn</strong>
        <p>Hymn #2 - "The Spirit of God"</p>
    </div>
</div>
```

To change the opening hymn, update:
- The time (if needed): `11:00 AM`
- The hymn number and name: `Hymn #2 - "The Spirit of God"`

## Step 3: Update Speakers

Find speaker sections and update the name and topic:
```html
<div class="agenda-item">
    <span class="time">11:30 AM</span>
    <div class="details">
        <strong>Speaker</strong>
        <p>Sister Johnson - "Faith in Jesus Christ"</p>
    </div>
</div>
```

Change to:
```html
<div class="agenda-item">
    <span class="time">11:30 AM</span>
    <div class="details">
        <strong>Speaker</strong>
        <p>Brother Lee - "Service to Others"</p>
    </div>
</div>
```

## Step 4: Update Announcements

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

## Step 5: Update the Footer Date

Find this line at the bottom (around line 146):
```html
<p class="update-info">Last updated: October 22, 2025</p>
```

Change to today's date:
```html
<p class="update-info">Last updated: October 29, 2025</p>
```

## Step 6: Save and Upload

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
