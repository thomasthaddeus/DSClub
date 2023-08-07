# Front Page

## Changes

### 1. `header.html`

```html
<header>
    <nav style="display: flex; justify-content: space-between; padding: 10px 0;">
        <a href="{{ '/' | relative_url }}" style="font-weight: bold;">{{ site.title }}</a>
        <div style="display: flex; gap: 15px;"> <!-- Grouping links for better spacing -->
            <a href="{{ '/docs' | relative_url }}">Docs</a>
            <a href="{{ '/docs/workshops' | relative_url }}">Workshop</a>
            <a href="{{ '/docs/documentation' | relative_url }}">Documentation</a>
            <a href="{{ '/docs/Schedule.md' | relative_url }}">Schedule</a>
            <!-- Add more navigation links as needed -->
        </div>
    </nav>
</header>
```

### 2. `_sidebar.html`

```html
<div class="sidebar">
  <div class="sidebar-item" style="padding: 10px; margin-bottom: 15px;">
    <h2>Navigation</h2>
    <ul style="list-style-type: none; padding-left: 0;">
      <li><a href="{{ site.baseurl }}/index.html">Home</a></li>
      <li><a href="{{ site.baseurl }}/about.html">About</a></li>
      <li><a href="{{ site.baseurl }}/blog.html">Blog</a></li>
    </ul>
  </div>

  <div class="sidebar-item" style="padding: 10px; margin-bottom: 15px;">
    <h2>Categories</h2>
    <ul style="list-style-type: none; padding-left: 0;">
      {% for category in site.categories %}
        <li><a href="{{ site.baseurl }}/category/{{ category | first }}">{{ category | first }}</a></li>
      {% endfor %}
    </ul>
  </div>

  <div class="sidebar-item" style="padding: 10px;">
    <h2>Recent Posts</h2>
    <ul style="list-style-type: none; padding-left: 0;">
      {% for post in site.posts limit:5 %}
        <li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
      {% endfor %}
    </ul>
  </div>
</div>
```

### 3. `head_custom.html`

The script provided is already optimized for the "back to top" functionality. Ensure you have a styled button for this functionality in your main content or footer.

### 4. `footer.html`

```html
<footer style="background-color: #f5f5f5; padding: 10px 0; text-align: center;">
    <p>&copy; {{ site.time | date: '%Y' }} - {{ site.title }}</p>
    <!-- Social Media Links -->
    <div style="margin-top: 10px;">
        <a href="#" style="margin-right: 10px;"><img src="path_to_facebook_icon.png" alt="Facebook"></a>
        <a href="#" style="margin-right: 10px;"><img src="path_to_twitter_icon.png" alt="Twitter"></a>
        <a href="#"><img src="path_to_instagram_icon.png" alt="Instagram"></a>
    </div>
</footer>
```

**Note**: Replace `path_to_facebook_icon.png`, `path_to_twitter_icon.png`, and `path_to_instagram_icon.png` with the actual paths to your social media icons.

### Additional CSS

For hover effects and other styles, you might want to add the following CSS either in your main CSS file or within a `<style>` tag in the head of your HTML:

```css
a:hover {
    text-decoration: underline;
    color: #007BFF; /* Change this to your preferred hover color */
}

.sidebar-item {
    border: 1px solid #e0e0e0;
    border-radius: 5px;
}

.sidebar-item h2 {
    background-color: #f5f5f5;
    padding: 5px 10px;
    margin-top: 0;
}
```
