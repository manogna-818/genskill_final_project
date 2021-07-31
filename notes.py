import datetime
from flask import Flask
from flask import Blueprint
from flask import render_template, request, redirect, url_for, jsonify
from flask import g
import psycopg2
dbconn=psycopg2.connect("dbname=final_project")

bp=Flask("notemaker")
def format_date(d):
    if d:
        d = datetime.datetime.strptime(d, '%Y-%m-%d')
        v = d.strftime("%a - %b %d, %Y")
        return v
    else:
        return None

@bp.route("/")  
def hello():
   cursor=dbconn.cursor()
   oby = request.args.get("order_by", "added") # TODO. This is currently not used. 
   order = request.args.get("order", "asc")
   if oby=="added":
        if order=="asc":
            cursor.execute("select id,name,added from note order by added")
        else:
            cursor.execute("select id,name,added from note order by added desc")
   get=cursor.fetchall()
   return render_template("mainpage.html", get = get,order="desc" if order=="asc" else "asc")
   
@bp.route("/<notenum>")
def note_details(notenum):
   cursor=dbconn.cursor()
   cursor.execute("select n.id,n.name,n.added,n.description from note n where n.id = (%s)",(notenum))
   get=cursor.fetchall()
   return render_template("desc.html",get=get)
   
@bp.route("/<notenum>/edit",methods=["GET","POST"])
def edit_details(notenum):
   cursor=dbconn.cursor()
   if request.method == "GET":
   	cursor.execute("select n.id,n.name,n.added,n.description from note n where n.id = (%s)",(notenum))
   	get=cursor.fetchall()
   	return render_template("edit_det.html",get=get)
   elif request.method == "POST":
        description = request.form.get('description')
        cursor.execute("update note set description=(%s) where id = (%s)",(description,notenum))
        name = request.form.get('name')
        cursor.execute("update note set name=(%s) where id = (%s)",(name,notenum))
        edited=datetime.datetime.now().strftime("%Y-%m-%d")
        cursor.execute("update note set added=(%s) where id =(%s)",(edited,notenum))
        dbconn.commit()
        return redirect(url_for("note_details",notenum=notenum),302)
        
        
 
 
