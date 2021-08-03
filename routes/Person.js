var express = require('express');
 var ejs = require("ejs")
 
var nodemailer = require('nodemailer');
var router = express.Router();
var db=require('../database');
// another routes also appear here
// this script to fetch data from MS SQL SERVER databAse table
router.get('/userapp', function(req, res, next) {
        
           
        
        db.query('select * from apdata' , function (err, data,fields) {
            
              if (err) throw err;
            
             console.log(data.recordset);
            
           
     
            db.query('select * from apdata WHERE Diastolic =(select max(Diastolic) from apdata)' , function (err, data1,fields) {
            
              if (err) throw err;
            
             console.log(data1.recordset);
 
             
              db.query( 'SELECT * FROM apdata WHERE Systolic > 130 AND Diastolic >90 AND Temp>37' , function (err, data2,fields) {
            
              if (err) throw err;
            
             console.log(data2.recordset);
                 
                    db.query('select TOP 1* from apdata' , function (err, data6,fields) {
            
              if (err) throw err;
            
             console.log(data6.recordset);      

var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'doctorjohospital@gmail.com',
    pass: '12345678doctorjo'
  }
});

var mailOptions = {
  from: 'doctorjohospital@gmail.com',
  to: 'joannagoub@gmail.com',
  subject: 'Alert',
   html: 'Watch your app for details'
};

transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});
              
             res.render('userapp', { title: 'User List',   userData :data.recordset, userData1 :data1.recordset , userData2: data2.recordset ,userData6: data6.recordset});
   
      });
     });
     });
  });
});
router.get('/delete/:id', function(req, res, next) {
  var id=req.params.id ;
      console.log(id);
  
    db.query( 'DELETE FROM apdata WHERE ID = id'  , function (err, data,fields) {
    if (err) throw err;
    console.log(data.affectedRows + " record(s) updated");
  });
  res.redirect('/Person/userapp');
  
});
// write here create & display data script
 
router.get('/edit/:id', function(req, res, next) {
      var UserId= req.params.id;
      var sql=`SELECT * FROM appdata WHERE ID= ?`;
      db.query(sql, [UserID],function (err, data) {
        if (err) throw err;
       
        res.render('userapp', { title: 'User List', editData: data[0]});
      });
});
router.post('/edit/:id', function(req, res, next) {
  var id= req.params.id;
    var updateData=req.body;
    var sql = `UPDATE appdata SET ? WHERE id= ?`;
    db.query(sql, [updateData, id], function (err, data) {
    if (err) throw err;
    console.log(data.affectedRows + " record(s) updated");
  });
  res.redirect('/Person/userapp');
});
router.get('/comment', function(req, res, next) {
  
 
   res.render('comment', { title: 'Comments'});
});

router.get('/maps1', function(req, res, next) {
  
   
   db.query('select * from Number  ' , function (err, data12,fields) {
            
              if (err) throw err;
            
             console.log(data12.recordset);
  
 
    res.render('maps1', { title: 'User List',   UserData12 :data12.recordset})
   });
   });
 router.get('/markerslocations', function(req, res, next) {
  
   
   db.query('select * from Number  ' , function (err, data12,fields) {
            
              if (err) throw err;
            
             console.log(data12.recordset);
  
 
    res.render('markerslocations', { title: 'User List',   UserData12 :data12.recordset})
   });
   });
  
router.get('/index1', function(req, res, next) {
  
 
   res.render('index1', { title: 'Dashboard'});
});

//login handle
router.get('/login',function(req, res, next){
    res.render('login');
});
router.get('/register',function(req, res){
    res.render('register')
    });
//Register handle
router.post('/register',function(req, res){

 res.redirect('/Person/userapp')
});
router.post('/login',function(req, res, next){
  res.redirect('/Person/userapp');
  });

//logout
router.get('/logout',(req,res)=>{
 });
module.exports = router;