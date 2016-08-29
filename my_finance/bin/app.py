import web
import psycopg2
import pygal

urls = (
 '/hello', 'Index'
)

#app = web.application(urls, globals())

try:
    conn = psycopg2.connect("dbname='my_finance' user='dbax' host='192.168.155.156' password='210482'")
except:
    print "Unable to connect to the database"

cur = conn.cursor()
cur.execute("""select account,round(sum(summ)) s from my_finance_tbls.my_transactions group by account order by s desc""")
rows = cur.fetchall()

pie_chart = pygal.Pie()
for row in rows:
   pie_chart.add('a', row[1])
#pie_chart.render(is_unicode=True)
pie_chart.render_to_file('/tmp/chart.svg')

#render = web.template.render('templates/')

#class Index(object):
#    def GET(self):
#        return render.hello_form()
#
#    def POST(self):
#        form = web.input(name="Nobody",greet="Hello")
#        greeting = "%s, %s" % (form.greet, form.name)
#        return render.index(greeting = greeting)

#if __name__ == "__main__":
#    app.run()
