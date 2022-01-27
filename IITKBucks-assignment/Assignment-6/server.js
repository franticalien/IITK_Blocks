
const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const http = require('http');
app.use(bodyParser.urlencoded({extended:true}));
app.use(express.static(__dirname+'/public'));

let resmap = new Map()
let peers = ['http:/www.google.com/add']



app.get("/list",(req,res)=>{
    

    

    const obj = Object.fromEntries(resmap)
    res.json(obj)
   
});



app.post("/add",(req,res)=>{
  console.log(req.body);

  console.log(typeof(req.body))

  for(let prop in req.body){
      if(!resmap.has(prop)){

                            
          resmap.set(prop,req.body[prop])
          for(let peer of peers){
              const options = {
                  method:'POST',
                  headers: {
                      'Content-type' : 'application/json'
                  }
              }
              const resstring = '{  \" ' + prop + '\" : \"  '+req.body[prop] + '\"}'
              const restopeer = JSON.parse(resstring)
             // const strrestopeer = JSON.parse(restopeer)

              
              const reqtopeer = http.request(peer,options,(res)=>{
                  console.log('request sent to ')
                  console.log(peer)
              });

              reqtopeer.write(resstring)
              reqtopeer.end()



              
          }


      }
      
  }

  //const json1 = JSON.parse(req.body)
  //console.log(json1)

  
  res.send("Thanks for the post")
});


app.listen(3000,()=>{
  console.log("server started on port 3000");
});
