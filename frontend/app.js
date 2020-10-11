const path=require("path")
const express=require('express')
const b=require("body-parser")
const app=express()
var EJS  = require('ejs');
const fileUpload = require('express-fileupload');
app.set("view engine",'ejs')
app.set('views', 'templates')
app.use(b.urlencoded({ extended: false }))
app.use(b.json())
app.use(fileUpload());
app.use(express.static(__dirname + '/public'))
const r=express.Router()
app.use('/scripts', express.static(__dirname + '/node_modules/bootstrap/dist/'));
app.get("/userPanel/indexx",(req,res)=>{
    return res.render("userpanel/index");
})
app.get("/createproduct",(req,res)=>{
    res.render("userpanel/createProduct")
})
app.get("/blogPost",(req,res)=>{
    res.render("userpanel/createBlogPost")
})
app.get("/addcat",(req,res)=>{
    res.render("userpanel/addCat")
})
app.get("/editcat",(req,res)=>{
    res.render("userpanel/editCat")
})
app.get("/sendticket",(req,res)=>{
    res.render("userpanel/ticket")
})
app.get("/alltickets",(req,res)=>{
    res.render("userpanel/ticketRep")
})
app.get("/myprods",(req,res)=>{
    res.render("userpanel/myprods")
})

app.get("/signup",(req,res)=>{
    res.render("account ejs/signup.ejs")
})
app.get("/signin",(req,res)=>{
    res.render("account ejs/signin.ejs")
})
app.listen(3001)