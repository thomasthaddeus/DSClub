# DS-Club

## Documentation

### What's included

- Ruby 2.6.6
- Rails 6.0.3
- SQLite3
- Node 12.16.1
- Yarn 1.22.4
- Bundler 2.1.4

### About Rails

Rails is a web-application framework that includes everything needed to create database-backed web applications according to the [Model-View-Controller (MVC)](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) pattern.

Understanding the MVC pattern is key to understanding Rails. MVC divides your application into three layers: Model, View, and Controller, each with a specific responsibility.

- The **Model** layer represents your domain model (such as Account, Product, Person, Post, etc.) and encapsulates the business logic that is specific to your application. In Rails, database-backed model classes are derived from `ActiveRecord::Base`. Active Record allows you to present the data from database rows as objects and embellish these data objects with business logic methods. Although most Rails models are backed by a database, models can also be ordinary Ruby classes, or Ruby classes that implement a set of interfaces as provided by the Active Model module.

The Codespace is running in a container with a full Ubuntu 20.04 environment. You have access to a full Linux terminal and all the tools you would expect. We've also pre-installed the [GitHub CLI](https://cli.github.com/) for you.

### Getting Started

The first thing you'll want to do is run `bundle install` to install all of the dependencies for your application. Once that's done you'll need to set up your database with `rails db:create db:migrate`. Finally, you can start up your Rails server with `rails server` and head over to the port 3000 on your codespace's URL to see your new Rails app live in action.

You can also run the Rails console with `rails console` or run any other Rails command.

You can get started by creating a new Rails app. Once you've created your app, you can run it using the following commands:

```sh
rails new myapp

cd myapp

# install the db
bundle install
rails db:create db:migrate db:seed
rails server

# or run the console
rails console
```

You can preview your app at <https://PORT-3000.YOUR-USERNAME.githubpreview.dev>

## Next Steps

- [x] Update this README to include information about your project
- [x] Build your app!
- [x] Push your code to GitHub
- [ ] Deploy your app to Heroku
- [ ] Share your app with friends!

## What's next?

- You can start a Rails server using `rails server`.
- You can preview the running application by clicking the "Open Ports" button at the bottom of the Codespace window and selecting port 3000.
- You can also open a terminal session in VS Code and run commands there.

## Structure

[Sitemap](./sitemap.html)

## Schedule

[Schedule](/docs/10_week_schedule.md)

## Notebooks

[Source](/src/notebooks/)

## Labs

[Workshops](/docs/workshops/)

## Meetings

Weekly on Wednesday's

## Links

- [Ruby on Rails](https://rubyonrails.org/)
- [Ruby on Rails guides](https://guides.rubyonrails.org/)
- [PostgreSQL](https://www.postgresql.org/docs/)
- [Ruby](https://www.ruby-lang.org/en/documentation/)
You can learn more about [developing in Codespaces](https://docs.github.com/en/codespaces/developing-in-codespaces) in the docs.
If you'd like to learn more about Codespaces, check out the [documentation](https://docs.github.com/en/github/developing-online-with-codespaces/creating-a-codespace).
If you're looking for more inspiration for what you can do with Codespaces, check out [the documentation](https://aka.ms/codespaces).
If you want to learn more about using Codespaces for Ruby on Rails then check out the [GitHub Docs](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace#creating-a-codespace-for-ruby-on-rails). You can also check out the [Ruby on Rails Guides](https://guides.rubyonrails.org/) for more information on using Rails.
[GitHub CLI](https://cli.github.com/)
[Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
