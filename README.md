# Madison YSA Agenda

A simple, clean website for displaying the weekly sacrament meeting agenda with helpful resource links.

## 🌐 View the Website

Once deployed, the website will be available at: `https://AMarkMartin.github.io/Madison-YSA-Agenda/`

## 📝 How to Update the Agenda Weekly

**Option 1: Use the Python Script (Recommended)**

The easiest way to update is using the automated `update_agenda.py` script:

1. Open `update_agenda.py` in any text editor
2. Edit the configuration section (lines 11-103):
   ```python
   WEEK_DATE = "October 29, 2025"
   
   QUOTE = {
       "text": "Your inspirational quote here",
       "citation": "Scripture Reference"
   }
   
   AGENDA_ITEMS = [
       {"title": "Opening Hymn", "description": "Hymn #2"},
       # ... add or modify items
   ]
   
   ANNOUNCEMENTS = [
       "Your announcement here",
       # ... add or modify announcements
   ]
   ```
3. Run the script to generate the updated HTML:
   ```bash
   python update_agenda.py
   ```
4. Commit and push:
   ```bash
   git add index.html update_agenda.py
   git commit -m "Update agenda for week of [DATE]"
   git push
   ```

**Option 2: Manual HTML Editing**

Alternatively, you can manually edit `index.html`:

1. Open `index.html` in any text editor
2. Update the date in the header:
   ```html
   <p class="date">Week of October 22, 2025</p>
   ```

3. Update the inspirational quote in the inspiration section:
   ```html
   <blockquote>
       <p>"Your inspirational quote here"</p>
       <cite>— Scripture Reference</cite>
   </blockquote>
   ```

4. (Optional) Add your own image by replacing the placeholder div:
   ```html
   <div class="inspiration-image">
       <img src="your-image-url.jpg" alt="Inspirational image">
   </div>
   ```

5. Modify the agenda items to match the week's schedule. Each agenda item looks like this:
   ```html
   <div class="agenda-item">
       <div class="details">
           <strong>Opening Hymn</strong>
           <p>Hymn #2 - "The Spirit of God"</p>
       </div>
   </div>
   ```

6. Update the announcements section as needed:
   ```html
   <li>Your announcement here</li>
   ```

7. Update the "Last updated" date in the footer:
   ```html
   <p class="update-info">Last updated: October 22, 2025</p>
   ```

8. Save the file and commit your changes:
   ```bash
   git add index.html
   git commit -m "Update agenda for week of [DATE]"
   git push
   ```

## 🚀 Deploying to GitHub Pages

To host your website on GitHub Pages:

1. Go to your repository on GitHub
2. Click on **Settings**
3. Scroll down to the **Pages** section (in the left sidebar)
4. Under **Source**, select the branch you want to deploy (usually `main` or `master`)
5. Select the root folder `/` 
6. Click **Save**
7. Wait a few minutes, and your site will be live!

Your website will be available at: `https://[your-username].github.io/Madison-YSA-Agenda/`

## 📋 Features

- **Clean, Modern Design**: Beautiful gradient header and card-based layout
- **Responsive**: Works perfectly on desktop, tablet, and mobile devices
- **Easy to Update**: Simple HTML structure makes weekly updates quick
- **Resource Links**: Quick access to important church resources
- **Announcements Section**: Highlight upcoming events and activities

## 🎨 Customization

### Changing Colors

The website uses a purple gradient theme. To change colors, edit `styles.css`:

- **Header gradient**: Look for `linear-gradient(135deg, #667eea 0%, #764ba2 100%)`
- **Accent colors**: Search for `#667eea` and `#764ba2` throughout the CSS

### Adding More Resources

To add more resource links, add a new link in the resources section of `index.html`:

```html
<a href="YOUR_URL" target="_blank" class="resource-link">
    <span class="link-icon">🔗</span>
    <span class="link-text">Your Link Name</span>
</a>
```

## 📱 Mobile Friendly

The website automatically adapts to different screen sizes, ensuring a great experience on phones and tablets.

## 🛠️ Technical Details

- Pure HTML and CSS (no build process required)
- No dependencies or frameworks needed
- Lightweight and fast loading
- Works in all modern browsers

## 📄 License

Feel free to use and modify this template for your ward or branch!
