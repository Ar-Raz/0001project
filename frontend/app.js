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
    return res.render("userPanelIndex");
})
app.get("/signup",(req,res)=>{
    return res.render("account_ejs/signup")
})
app.get("/token",(req,res)=>{
    res.render('confirmation')
})
app.get("/create",(req,res)=>{
    res.render("createProduct")
})
app.get("/order",(req,res)=>{
    res.render("miniOrders")
})
app.get("/ticket",(req,res)=>{
    res.render("ticket")
})
app.get("/category",(req,res)=>{
    res.render("addCat")
})
app.get("/blogpost",(req,res)=>{
    res.render("createBlogPost")
})
app.listen(3001)