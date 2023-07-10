---
title: Site Creation
subtitle: Documentation for what all the files are for
layout: default
theme: just-the-docs
---

## TODO: List

Set up Jekyll on GitHub Pages

- [ ] `_config.yml`: This is the main configuration file for your Jekyll website. It contains global configurations and variables for your site.
- [ ] `Gemfile`: This file is used by the Ruby dependency manager Bundler. It should specify the Jekyll gem and any other Ruby dependencies your site might have.
- [ ] `index.md` or `index.html`: This is the main content file for your site. It's what users will see when they go to the root URL of your site.
- [ ] `_posts` directory: This directory contains your blog posts. Each post should be a Markdown file with a filename in the format YEAR-MONTH-DAY-title.MARKUP.
- [ ] `_layouts` directory: This directory contains your layout templates. These are the common parts of your site that will be reused on multiple pages.
- [ ] `_includes` directory: This directory contains snippets of code that you can include in your layouts and posts.
- [ ] `_site` directory: This is where Jekyll will put the static HTML files it generates from your templates and posts. This directory should be ignored by Git, so you should have a .gitignore file that lists `_site`.
- [ ] `.github/workflows` directory (optional): If you want to use GitHub Actions to automatically build your site whenever you push changes, you can add a workflow file in this directory.
- [ ] `README.md` (optional): While not necessary for Jekyll or GitHub Pages, it's common practice to include a README file with information about your project.

**Other content files**: Besides the index file and posts, you can add other Markdown or HTML files for additional pages on your site. You can also add static files like images in a directory (often called assets or static).

Remember, when you're using GitHub Pages, you should have your Jekyll site on the gh-pages branch if it's a project page, or on the master branch if it's a user or organization page.
