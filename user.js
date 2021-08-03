const mssql = require('mssql/msnodesqlv8'); 

const UserSchema  = new mssql.Schema({
  name :{
      type  : String,
      required : true
  } ,
  email :{
    type  : String,
    required : true
} ,
password :{
    type  : String,
    required : true
} ,
date :{
    type : Date,
    default : Date.now
}
});
const User= mssql.model('User',UserSchema);
 // config for your database
    var config = {
     database:'Users',  
  server: 'localhost\\SQLEXPRESS',
  driver: 'msnodesqlv8',
  options: {
    trustedConnection: true,
    enableArithAbort: true
    }

  
    };

    // connect to your database
   User= mssql.connect(config, function (err) {
    
        if (err) throw err;

       
       console.log('Database is connected successfully !');
            return User;
        });
     
module.exports = User;