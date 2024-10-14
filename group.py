"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {'Jill': 
            {'age': 26, 
            'job': 'biologist', 
            'connection':{
                'friend': 'Zalika',
                'partner': 'John'
            }
            },
            'Zalika':
            {'age': 28,
             'job': 'artist',
             'connection':{
                 'friend': 'Jill'
             }
             },
             'John':
             {'age': 27,
              'job': 'writer',
              'connection': {
                  'partner': 'Jill'
              }
              },
            'Nash':
            {'age': 34,
             'job': 'chef',
             'connection': {
                 'cousin': 'John',
                 'landlord': 'Zalika'
             }

            }  
}


