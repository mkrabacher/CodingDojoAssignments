var users = {
    'Students': [ 
        {first_name:  'Michael', last_name : 'Jordan'},
        {first_name : 'John', last_name : 'Rosales'},
        {first_name : 'Mark', last_name : 'Guillen'},
        {first_name : 'KB', last_name : 'Tonel'}
     ],
    'Instructors': [
        {first_name : 'Michael', last_name : 'Choi'},
        {first_name : 'Martin', last_name : 'Puryear'}
     ]
    }

function parentsJob(arr) {
    for (role in users) {
        console.log(role)
        for(i = 0; i < users[role].length; i++) {
            var fullName = (users[role][i].first_name + " " + users[role][i].last_name)
            console.log(i + " - " + fullName + " - " + fullName.length)
        }
    }
}

parentsJob();