import cherrypy
import MySQLdb
import random, time

db = MySQLdb.connect(host="localhost",
                        user="root",
                        passwd="bloodston3",
                        db= "cherrydb")

cur = db.cursor()

@cherrypy.expose
class StringGeneratorWebService(object):


    @cherrypy.tools.accept(media='text/plain')        
    def GET(self, name="second", another="1"):
        cur.execute("SELECT * FROM alpha")
        rows = cur.fetchall()
        template = ""
        for row in rows:
            template += '<p style="color: blue;">' + str(row[0]) + ' : ' + str(row[1]) + '</p>'
        return template
        


    def POST(self, length=8):
        some_string = 'Something dynamic'
        return some_string

    def PUT(self, name="test"):
        rowsWritten = cur.execute("INSERT INTO alpha VALUES (%s, %s)", (name, "then"))
        db.commit()
        return rowsWritten

    def DELETE(self):
       return 'delete'


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Access-Control-Allow-Origin', '*')]
        }
    }
    cherrypy.config.update({'server.socket_port': 9090})
    cherrypy.quickstart(StringGeneratorWebService(), '/', conf)
    db.commit()
    db.close()