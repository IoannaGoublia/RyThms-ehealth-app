const mssql = require('mssql/msnodesqlv8'); 

    // config for your database
    var config = {
     database:'TestDB',  
  server: 'localhost\\SQLEXPRESS',
  driver: 'msnodesqlv8',
  options: {
    trustedConnection: true,
    enableArithAbort: true
    }

  
    };

    // connect to your database
   z= mssql.connect(config, function (err) {
    
        if (err) throw err;

       
       console.log('Database is connected successfully !');
            return z;
        });
     module.exports=z;