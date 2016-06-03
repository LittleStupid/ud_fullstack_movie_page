class Movie():
    """ This class stores movie information."""

    #Movie store title, image url, trailer url.
    def __init__( self, title, poster_image_url, trailer_youtube_url ):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

#create 3 movies.
xmen = Movie( 'X-Men: Apocalypse',
              'http://cdn2-www.comingsoon.net/assets/uploads/gallery/bts-x-men-apocalypse/cf7kkqeuuaeqame.jpg',
              'https://www.youtube.com/watch?v=COvnHv42T-A')
transformers = Movie( 'Transformers',
                      'http://www.hometheaterseattle.com/assets/images/movies/transformers-2-revenge-of-the-fallen-movie-2009.jpg',
                      'https://www.youtube.com/watch?v=gAjgXlvVexI')
superman_vs_batman = Movie( 'Batman v Superman',
                          'https://www.movie-list.com/img/posters/big/zoom/batmanvsuperman.jpg',
                          'https://www.youtube.com/watch?v=ES3INFYuTcI')

#set movies into a list.
movies = []
movies.append( xmen )
movies.append( transformers )
movies.append( superman_vs_batman )
