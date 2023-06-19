# @name: attempt.py
# @author: bartramj025070

import random
import json

window_x = 600
window_y = 600

# overwrites the save data with default ones
def clear_save():
    dat = {
        "fruit": {
            "x": random.randrange(1, (window_x//10)) * 10,
            "y": random.randrange(1, (window_y//10)) * 10
        },
        
        "difficulty": "NORMAL",
        "score": 0,
        "snake": {
            "speed": 10,
            "position": [100, 50],
            "body": [[100, 50],
                      [90, 50],
                      [80, 50],
                      [70, 50]
                      ],
            "direction": 'RIGHT'
        }
    }
    
    with open('save.json', 'w') as f:
        f.write(json.dumps(dat))

clear_save()