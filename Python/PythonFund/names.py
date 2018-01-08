users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan', 'number':13},
     {'first_name' : 'John', 'last_name' : 'Rosales', 'number':11},
     {'first_name' : 'Mark', 'last_name' : 'Guillen', 'number':11},
     {'first_name' : 'KB', 'last_name' : 'Tonel', 'number':7}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi', 'number':11},
     {'first_name' : 'Martin', 'last_name' : 'Puryear', 'number':13}
  ]
 }


def nems(dic):
    for dept in dic:
        print dept
        num = 1
        for user in users[dept]:
            # print user
            print '{} - {} {} - {}'.format(num, user['first_name'], user['last_name'], user['number']).upper()
            num += 1

nems(users)