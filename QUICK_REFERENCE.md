# Quick Reference - Weekly Update Checklist

Use this as a quick checklist when updating the agenda each week.

## 🐍 Python Script Method (Recommended)

**Fastest and easiest method:**

1. Edit `update_agenda.py` (lines 11-103):
   - Update `WEEK_DATE`
   - Update `QUOTE` 
   - Modify `AGENDA_ITEMS`
   - Update `ANNOUNCEMENTS`
2. Run: `python update_agenda.py`
3. Commit: 
   ```bash
   git add index.html update_agenda.py
   git commit -m "Update agenda for week of [DATE]"
   git push
   ```

**See `EXAMPLE_UPDATE.md` for detailed examples.**

---

## ✅ Manual HTML Update Checklist

If you prefer to edit HTML directly:

- [ ] Update header date (line ~14): `Week of [DATE]`
- [ ] Update inspirational quote (line ~20-22)
- [ ] (Optional) Add custom image to replace placeholder
- [ ] Update opening hymn
- [ ] Update invocation speaker
- [ ] Update sacrament hymn
- [ ] Update speaker 1 (name & topic)
- [ ] Update musical number (if any)
- [ ] Update speaker 2 (name & topic)
- [ ] Update closing hymn
- [ ] Update benediction speaker
- [ ] Update announcements (add/remove as needed)
- [ ] Update footer date (line ~158): `Last updated: [DATE]`
- [ ] Save file
- [ ] Commit and push changes

## 🔍 Quick Find

Search for these in `index.html`:
- `Week of` - Header date
- `inspiration-quote` - Inspirational quote section
- `placeholder-image` - Image placeholder (to add custom image)
- `Opening Hymn` - First agenda item
- `Announcements` - Section for announcements
- `Last updated` - Footer date

## 📤 Git Commands

```bash
git add index.html
git commit -m "Update agenda for week of [DATE]"
git push
```

## 💡 Tips

- Copy an existing agenda-item block when adding new items
- Use Ctrl+F (or Cmd+F on Mac) to quickly find sections
- Preview your changes locally before committing
- Keep the HTML structure intact - only change the text

---

For detailed instructions with examples, see `UPDATE_GUIDE.md`
