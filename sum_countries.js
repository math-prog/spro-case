// create connection with mongodb
var conn = new Mongo("mongodb://127.0.0.1:27017/");

// connect to database
var db = conn.getDB("spro_case");

// aggregate pipeline
var pipeline = [
    {
        $lookup: {
            from: 'montadoras',
            localField: 'montadora',
            foreignField: 'montadora',
            as: 'montadoras'
        }
    }, {
        $addFields: {
            pais: {
                $arrayElemAt: [
                    '$montadoras.pais',
                    0
                ]
            },
            montadoras: {
                $size: '$montadoras'
            }
        }
}, {
        $group: {
            _id: '$pais',
            quantidade_de_carros: {
                $sum: 1
            }
    } 
}];

// execute pipeline and store result in a new collection
db.carros.aggregate(pipeline, { $out: "carros_montadoras_pais" });

// close connection
conn.close();

