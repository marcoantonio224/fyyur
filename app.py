#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from flask_migrate import Migrate
from forms import *
import sys
import re
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
# Create a migrate connection for app
migrate = Migrate(app, db)

# TODO: connect to a local postgresql database

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(120), nullable=False)
    facebook_link = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.String(500), nullable=False)
    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    website = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(120))
    past_shows_count = db.Column(db.Integer, default=0)
    upcoming_shows_count = db.Column(db.Integer, default=0)
    # Create a relationship for Show models
    show = db.relationship('Show', cascade='all, delete-orphan', backref='venue', lazy=True)
    # venues = db.relationship('Show', backref='venue', lazy=True)




class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.String(500), nullable=False)
    website = db.Column(db.String(120), nullable=True)
    image_link = db.Column(db.String(120), nullable=True)
    facebook_link = db.Column(db.String(120), nullable=False)
    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    seeking_venue = db.Column(db.BOOLEAN, default=False)
    past_shows_count = db.Column(db.Integer, default=0)
    upcoming_shows_count = db.Column(db.Integer, default=0)
    # Create a relationship for Show models
    show = db.relationship('Show', cascade='all, delete-orphan', backref='artist', lazy=True)



# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

class Show(db.Model):
  __tablename__ = 'shows'
  id = db.Column(db.Integer, primary_key=True)
  artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
  venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)
  artist_image_link = db.Column(db.String(120), nullable=False)
  start_time = db.Column(db.String(120), nullable=False)

db.create_all()
#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format)

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

# Handle errors in api requests
def handleError():
    db.session.rollback()
    print(sys.exc_info())

@app.route('/')
def index():
  return render_template('pages/home.html')


#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
  # TODO: replace with real venues data.
  #       num_shows should be aggregated based on number of upcoming shows per venue.
  data = Venue.query.all() # Get Venues
  dataArr = [] # Organize Venues by city
  # Create and store keys for each city
  venuesMaster = {}
  for obj in data:
    venuesMaster[obj.city] = obj.city
  # Loop through each city in venuesMaster dictionary
  for city in venuesMaster:
    # Create a dictionary for a city
    venue = {'venues':[]}
    # Group cities together
    res = Venue.query.filter_by(city=city).all()
    # Create proper values for each dictionary
    venue['city'] = res[0].city
    venue['state'] = res[0].state
    # Now append each dictionary by their proper cities
    for obj in res:
      x = {'id':obj.id, 'name': obj.name, 'upcoming_shows_count': obj.upcoming_shows_count}
      venue['venues'].append(obj)
    dataArr.append(venue)

  return render_template('pages/venues.html', areas=dataArr)

@app.route('/venues/search', methods=['POST'])
def search_venues():
  # TODO: implement search on venues with partial string search. Ensure it is case-insensitive.
  # seach for Hop should return "The Musical Hop".
  # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"
  data = Venue.query.all()
  response= {'count':0, 'data': []}
  pattern = request.form.get('search_term')
  for venue in data:
    if pattern.lower() in venue.name.lower():
      response['count']+=1
      venueDict = {}
      venueDict['id'] = venue.id
      venueDict['name'] = venue.name
      venueDict['upcoming_shows_count'] = venue.upcoming_shows_count
      response['data'].append(venueDict)
  return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  # shows the venue page with the given venue_id
  data = Venue.query.filter_by(id=venue_id).one() # GET VENUES BY SEARCH QUERY
  # Create regular expression for }{" and remove special characters and convert them into a list
  genres = re.sub(r'[{}"]+', '', data.genres).split(',')
  # Split the values for genres
  data.genres = genres
  return render_template('pages/show_venue.html', venue=data)

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion
  try:
    name = request.form['name']
    city = request.form['city']
    address = request.form['address']
    state = request.form['state']
    phone = request.form['phone']
    genres = request.form.getlist('genres')
    image_link =''
    facebook_link = request.form['facebook_link']
    venue = Venue(name = name, city = city, state=state, address = address, phone = phone, genres = genres, image_link = image_link, facebook_link=facebook_link)
    db.session.add(venue)
    db.session.commit()
     # on successful db insert, flash success
    flash('Venue ' + request.form['name'] + ' was   successfully listed!')
  except:
    # e.g., flash('An error occurred. Venue ' + request.form['name'] + ' could not be listed.')
    # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
    flash('An error occured. Venue ' + request.form['name'] + ' could not be listed.')
    handleError()
  finally:
    db.session.close()

  return render_template('pages/home.html')

@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
  # TODO: Complete this endpoint for taking a venue_id, and using
  # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.
  try:
    venue = Venue.query.filter_by(id=venue_id).one()
    db.session.delete(venue)
    db.session.commit()
    flash('Venue ' + venue.name + ' was   successfully deleted!')
  except:
    # e.g., flash('An error occurred. Venue ' + request.form['name'] + ' could not be listed.')
    # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
    flash('An error occured. Venue ' + request.form['name'] + ' could not be deleted.')
    handleError()
  finally:
    db.session.close()
  # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage
  return jsonify({"hello":'m'})


#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
  # TODO: replace with real data returned from querying the database
  data= Artist.query.all() # GET ARTISTS
  return render_template('pages/artists.html', artists=data)

@app.route('/artists/search', methods=['POST'])
def search_artists():
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
  # search for "band" should return "The Wild Sax Band".
  data = Artist.query.all()
  response= {'count':0, 'data': []} # GET DICTIONARY RESPONSE
  pattern = request.form.get('search_term')
  for artist in data:
    if pattern.lower() in artist.name.lower():
      response['count']+=1
      artistDict = {}
      artistDict['id'] = artist.id
      artistDict['name'] = artist.name
      artistDict['upcoming_shows_count'] = artist.upcoming_shows_count
      response['data'].append(artistDict)
  return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  # shows the venue page with the given venue_id
  # TODO: replace with real venue data from the venues table, using venue_id
  data = Artist.query.filter_by(id=artist_id).one() # GET ARTIST BY ID
  # Create regular expression for }{" and remove special characters and convert them into a list
  genres = re.sub(r'[{}"]+', '', data.genres).split(',')
  # Split the values for genres
  data.genres = genres
  return render_template('pages/show_artist.html', artist=data)

#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  form = ArtistForm()
  artist = Artist.query.filter_by(id=artist_id).one() # GET ARTIST
  # TODO: populate form with fields from artist with ID <artist_id>
  return render_template('forms/edit_artist.html', form=form, artist=artist)

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  # TODO: take values from the form submitted, and update existing
  # artist record with ID <artist_id> using the new attributes
  try:
    artist = Artist.query.filter_by(id=artist_id).one()
    artist.name = request.form['name']
    artist.city = request.form['city']
    artist.state = request.form['state']
    artist.phone = request.form['phone']
    artist.genres = request.form.getlist('genres')
    artist.facebook_link = request.form['facebook_link']
    db.session.commit()
     # on successful db insert, flash success
    flash('Artist ' + request.form['name'] + ' was successfully edited!')
  except:
    # TODO: on unsuccessful db insert, flash an error instead.
    # e.g., flash('An error occurred. Artist ' + request.form['name'] + ' could not be listed.')
    flash('An error occurred. Artist '+ request.form['name'] + ' could not be edited.')
    handleError()
  finally:
    db.session.close()
  return redirect(url_for('show_artist', artist_id=artist_id))

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  form = VenueForm()
  venue = Venue.query.filter_by(id=venue_id).one() # GET VENUE BY ID
  # TODO: populate form with values from venue with ID <venue_id>
  return render_template('forms/edit_venue.html', form=form, venue=venue)

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  # TODO: take values from the form submitted, and update existing
  # venue record with ID <venue_id> using the new attributes
  try:
    venue = Venue.query.filter_by(id=venue_id).one()
    venue.name = request.form['name']
    venue.city = request.form['city']
    venue.state = request.form['state']
    venue.phone = request.form['phone']
    venue.genres = request.form.getlist('genres')
    venue.facebook_link = request.form['facebook_link']
    db.session.commit()
     # on successful db insert, flash success
    flash('Venue ' + request.form['name'] + ' was successfully edited!')
  except:
    # TODO: on unsuccessful db insert, flash an error instead.
    # e.g., flash('An error occurred. Artist ' + request.form['name'] + ' could not be listed.')
    flash('An error occurred. Artist '+ request.form['name'] + ' could not be edited.')
    handleError()
  finally:
    db.session.close()

  return redirect(url_for('show_venue', venue_id=venue_id))

#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  # called upon submitting the new artist listing form
  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion
  try:
    name = request.form['name']
    city = request.form['city']
    state = request.form['state']
    phone = request.form['phone']
    genres = request.form.getlist('genres')
    image_link ='IMAGE LINK EXAMPLE'
    facebook_link = request.form['facebook_link']
    artist = Artist(name=name, city=city, state=state, phone=phone, genres=genres, image_link=image_link, facebook_link=facebook_link)
    db.session.add(artist)
    db.session.commit()
     # on successful db insert, flash success
    flash('Artist ' + request.form['name'] + ' was successfully listed!')
  except:
    # TODO: on unsuccessful db insert, flash an error instead.
    # e.g., flash('An error occurred. Artist ' + request.form['name'] + ' could not be listed.')
    flash('An error occurred. Artist '+ request.form['name'] + ' could not be listed.')
    handleError()

  finally:
    db.session.close()

  return render_template('pages/home.html')


#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  # displays list of shows at /shows
  # TODO: replace with real venues data.
  #       num_shows should be aggregated based on number of upcoming shows per venue.
  shows = Show.query.all()
  results = []
  for show in shows:
    artist = Artist.query.filter_by(id=show.artist_id).one()
    venue = Venue.query.filter_by(id=show.venue_id).one()
    showObject = {}
    showObject['start_time'] = show.start_time
    showObject['artist_name'] = artist.name
    showObject['venue_name'] = venue.name
    results.append(showObject)

  return render_template('pages/shows.html', shows=results)

@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  # called to create new shows in the db, upon submitting new show listing form
  # TODO: insert form data as a new Show record in the db, instead
  try:
    artist_id = request.form['artist_id']
    venue_id = request.form['venue_id']
    start_time = request.form['start_time']
    artist_obj = Artist.query.filter_by(id=artist_id).all()
    # Grab the artist link
    link = ''
    for row in artist_obj:
      link = row.image_link
    artist_image_link = link
    show = Show(artist_id = artist_id, artist_image_link = artist_image_link, venue_id = venue_id,start_time = start_time)
    db.session.add(show)
    db.session.commit()
    # on successful db insert, flash success
    flash('Show was successfully listed!')
  except:
    # TODO: on unsuccessful db insert, flash an error instead.
    # e.g., flash('An error occurred. Show could not be listed.')
    flash('An error occurred. Show could not be listed.')
    handleError()
  finally:
    db.session.close()
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  return render_template('pages/home.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
