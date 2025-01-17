const express = require('express')
const app = express()
const PORT = 3000
app.use(express.urlencoded({extended: true}));
app.use(express.json())

app.listen(PORT, () => {
console.log('running...')
})

let db = [
{
id: 1,
firstName: 'John',
lastName: 'Doe',
email: 'jd@example.com'
},
{
id: 2,
firstName: 'J',
lastName: 'D',
email: 'jd@example.com'
}
]

app.get('/users', (req, res) => {
res.json(db)
})

app.post('/users', (req, res) => {
let lastId = Math.max(...db.map(u => u.id))
const user = {
id: ++lastId,
firstName: req.body.fName,
lastName: req.body.lName,
email: req.body.e
}
db.push(user)
res.json(db)
})

app.get('/users/:id', (req,res) => {
let user = db.find(u => u.id===parseInt(req.params.id))
res.json(user)
})

app.delete('/users/:id', (req, res) => {
db = db.filter(u => u.id !== parseInt(req.params.id))
res.json(db)
})