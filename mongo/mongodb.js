mongo "mongodb+srv://cluster0.t3c6s.mongodb.net/pap_database" --username admin --password admin --eval "db.annonce_pap.aggregate([{\$group:{_id:\"$ref\", annonce_pap:{\$push:\"$_id\"}, count: {\$sum: 1}}}, 
{\$match:{count: {\$gt: 1}}} ]).forEach(function(doc){   doc.annonce_pap.pop();   
db.annonce_pap.remove({_id : {\$in: doc.annonce_pap}}); });"
