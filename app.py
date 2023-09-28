from flask import Flask,session,render_template,url_for,request,send_file
from werkzeug.utils import secure_filename
import os
from zipfile import ZipFile
app=Flask(__name__,template_folder="designs",static_folder="upload_folder")
app.config["SECRET_KEY"]="1234567890"
app.config["UPLOAD_FOLDER"]="template/upload_folder"
@app.route("/style")
def style():
    return render_template("style.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/banking")
def banking():
    return render_template("banking.html")

@app.route("/E_commerce")
def E_commerce():
    return render_template("E_commerce.html")

@app.route("/homepage")
def Homepage():
    return render_template("homepage.html")

@app.route("/streaming")
def streaming():
    return render_template("streaming.html")

@app.route("/College")
def College():
    return render_template("college.html")

@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/pd1")
def pd1():
    return render_template("pd1.html")

@app.route("/pd2")
def pd2():
    return render_template("pd2.html")

@app.route("/pd3")
def pd3():
    return render_template("pd3.html")

@app.route("/index")
def input():
    return render_template("index.html")

@app.route("/pd1out",methods=["Post"])
def pd1output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/pd1/images/"+filename)
        session["data"]=filename
        a =render_template("./pd1out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html",design=design)
    else:
        return render_template("pd1.html",problem="Only Jpg or png files")
@app.route("/pd2out",methods=["Post"])
def pd2output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    college=request.form["College"]
    city=request.form["city"]
    snap=request.form["snapchat"]
    gmail=request.form["gmail"]
    skill1=request.form["skill1"]
    skill2=request.form["skill2"]
    skill3=request.form["skill3"]
    skill4=request.form["skill4"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/pd2/images/"+filename)
        session["data"]=filename
        a =render_template("./pd2out.html",img =filename,gmail=gmail,city=city,skill1=skill1,skill2=skill2,skill3=skill3,skill4=skill4,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html",design=design)
    else:
        return render_template("pd2.html",problem="Only Jpg or png files")
@app.route("/pd3out",methods=["Post"])
def pd3output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    about=request.form["about"]
    skill=request.form["skill"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/pd3/images/"+filename)
        session["data"]=filename
        a =render_template("./pd3out.html",img =filename,about=about,skill=skill,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html",design=design)
    else:
        return render_template("pd3.html",problem="Only Jpg or png files")
@app.route("/ec1out",methods=["Post"])
def ec1output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/ec1/images/"+filename)
        session["data"]=filename
        a =render_template("./ec1out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html")
    else:
        return render_template("ec1.html",problem="Only Jpg or png files")
@app.route("/ec2out",methods=["Post"])
def ec2output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/ec2/images/"+filename)
        session["data"]=filename
        a =render_template("./ec2out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html")
    else:
        return render_template("ec1.html",problem="Only Jpg or png files")
@app.route("/ec3out",methods=["Post"])
def ec3output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/ec3/images/"+filename)
        session["data"]=filename
        a =render_template("./ec3out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html")
    else:
        return render_template("ec3.html",problem="Only Jpg or png files")
@app.route("/bk1out",methods=["Post"])
def bk1output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/bk1/images/"+filename)
        session["data"]=filename
        a =render_template("./bk1out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html")
    else:
        return render_template("bk1.html",problem="Only Jpg or png files")
@app.route("/bk2out",methods=["Post"])
def bk2output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/bk2/images/"+filename)
        session["data"]=filename
        a =render_template("./bk2out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html")
    else:
        return render_template("bk2.html",problem="Only Jpg or png files")
@app.route("/bk3out",methods=["Post"])
def bk3output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/bk3/images/"+filename)
        session["data"]=filename
        a =render_template("./bk3out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html")
    else:
        return render_template("bk3.html",problem="Only Jpg or png files")
@app.route("/hp1out",methods=["Post"])
def hp1output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/hp1/images/"+filename)
        session["data"]=filename
        a =render_template("./hp1out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html")
    else:
        return render_template("hp1.html",problem="Only Jpg or png files")
@app.route("/hp2out",methods=["Post"])
def hp2output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/hp2/images/"+filename)
        session["data"]=filename
        a =render_template("./hp1out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html")
    else:
        return render_template("hp2.html",problem="Only Jpg or png files")
@app.route("/hp3out",methods=["Post"])
def hp3output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/hp3/images/"+filename)
        session["data"]=filename
        a =render_template("./hp3out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html")
    else:
        return render_template("hp3.html",problem="Only Jpg or png files")
@app.route("/st1out",methods=["Post"])
def st1output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/st1/images/"+filename)
        session["data"]=filename
        a =render_template("./st1out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html")
    else:
        return render_template("st1.html",problem="Only Jpg or png files")
@app.route("/st2out",methods=["Post"])
def st2output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/st1/images/"+filename)
        session["data"]=filename
        a =render_template("./st2out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html")
    else:
        return render_template("st2.html",problem="Only Jpg or png files")
    
@app.route("/st3out",methods=["Post"])
def st3output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/st3/images/"+filename)
        session["data"]=filename
        a =render_template("./st3out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html")
    else:
        return render_template("st3.html",problem="Only Jpg or png files")

@app.route("/cg1out",methods=["Post"])
def cg1output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/cg1/images/"+filename)
        session["data"]=filename
        a =render_template("./cg2out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html")
    else:
        return render_template("cg1.html",problem="Only Jpg or png files")
@app.route("/cg2out",methods=["Post"])
def cg2output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/cg2/images/"+filename)
        session["data"]=filename
        a =render_template("./cg2out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html")
    else:
        return render_template("cg2.html",problem="Only Jpg or png files")
@app.route("/cg3out",methods=["Post"])
def cg3output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/cg3/images/"+filename)
        session["data"]=filename
        a =render_template("./cg3out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html")
    else:
        return render_template("cg3.html",problem="Only Jpg or png files")
@app.route("/ed1out",methods=["Post"])
def ed1output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/ed1/images/"+filename)
        session["data"]=filename
        a =render_template("./ed1out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html")
    else:
        return render_template("ed1.html",problem="Only Jpg or png files")
@app.route("/ed2out",methods=["Post"])
def ed2output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/ed2/images/"+filename)
        session["data"]=filename
        a =render_template("./ed2out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html")
    else:
        return render_template("ed2.html",problem="Only Jpg or png files")
@app.route("/ed3out",methods=["Post"])
def ed3output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/ed3/images/"+filename)
        session["data"]=filename
        a =render_template("./ed3out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html",design=design)
    else:
        return render_template("ed3.html",problem="Only Jpg or png files")
@app.route("/cga1out",methods=["Post"])
def ga1output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/ga1/images/"+filename)
        session["data"]=filename
        a =render_template("./ga1out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html")
    else:
        return render_template("ga1.html",problem="Only Jpg or png files")
@app.route("/ga2out",methods=["Post"])
def ga2output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/ga2/images/"+filename)
        session["data"]=filename
        a =render_template("./ga2out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html")
    else:
        return render_template("ga2.html",problem="Only Jpg or png files")
@app.route("/ga3out",methods=["Post"])
def ga3output():
    fname=request.form["name"]
    lname=request.form["lname"]
    occupation=request.form["occupation"]
    resume=request.form["resume"]
    desc=request.form["desc"]
    file = request.files["image"]
    insta=request.form["insta"]
    linkedin=request.form["linkedin"]
    design=request.form["design"]
    if ".png" in file.filename or ".jpg" in file.filename or ".jpeg" in (file.filename).lower() or ".webp" in (file.filename).lower() :
        filename=secure_filename(file.filename)
        file.save("template/upload_folder/static/ga3/images/"+filename)
        session["data"]=filename
        a =render_template("./ga3out.html",img =filename,fname=fname,lname=lname,desc=desc,insta=insta,linkedin=linkedin,occupation=occupation,resume=resume,design=design)
        file=open("template/designs/new.html","w")
        file.write(a)
        file.close()
        return render_template("output.html")
    else:
        return render_template("ga3.html",problem="Only Jpg or png files")
@app.route("/new")
def new():
    return render_template("new.html")
@app.route("/about")
def about():
    return render_template("about.html") 
@app.route("/search")
def search():
    search=request.form["search"].strip().lower()
    if search=="portfolio":
        return render_template("portfolio.html")
    elif search =="streaming":
        return render_template("streaming.html")
    elif search=="gallery":
        return render_template("gallery.html")
    elif search=="ecommerce":
        return render_template("E_commerce.html")
    elif search =="college":
        return render_template("college")
    elif "banking" in search:
        return render_template("bank")
    elif search=="homepage":
        return render_template("homepage.html")
    elif search =="education":
        return render_template("education.html")
@app.route("/downloadpd1")
def downloadpd1():
    with ZipFile("new.zip","w") as zipped:
        zipped.write("./template/designs/new.html")
        zipped.write("./template/upload_folder/static/pd1/pd1.css")
        zipped.write("./template/upload_folder/static/pd1/images/instagram.png")
        zipped.write("./template/upload_folder/static/pd1/images/pngwing.com (1).png")
        zipped.write(f"./template/upload_folder/static/pd1/images/{session.get('data')}")
        os.remove("./template/designs/new.html")
        os.remove(f"./template/upload_folder/static/pd1/images/{session.get('data')}")
        return send_file("./new.zip",as_attachment=True,download_name="viewflex.zip")
@app.route("/downloadpd2")
def downloadpd2():
    with ZipFile("new.zip","w") as zipped:
        zipped.write("./template/designs/new.html")
        zipped.write("./template/upload_folder/static/pd2/pd2.css")
        zipped.write(f"./template/upload_folder/static/pd2/images/{session.get('data')}")
        os.remove("./template/designs/new.html")
        os.remove(f"./template/upload_folder/static/pd2/images/{session.get('data')}")
        return send_file("new.zip",as_attachment=True,download_name="viewflex.zip")
@app.route("/downloadpd3")
def downloadpd3():
    with ZipFile("./template\new.zip","w") as zipped:
        zipped.write("./template/designs/new.html")
        zipped.write("./template/upload_folder/static/pd3/pd3.css")
        zipped.write(f"./template/upload_folder/static/pd3/images/{session.get('data')}")
        os.remove("./template/designs/new.html")
        os.remove(f"./template/upload_folder/static/pd3/images/{session.get('data')}")
        return send_file ("./template\new.zip", as_attachment=True,download_name="viewflex.zip")
@app.route("/contact")
def contact():
    return render_template("contact.html")
app.run(debug=True)
