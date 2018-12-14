from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
global car_dictionary
car_dictionary = dict()
vacated = list()
i = 1


@app.route('/')
def index():
    return render_template('form.html')

@app.route('/parking', methods= ['POST'])
def parking():
    
    reg_no = request.form['email']
    if reg_no:

        view = reg_no.split(' ')
        print(view)
        text = str(view[0])
        if text == 'park' or text == 'Park':
            global i
            global vacated
            if len(car_dictionary) <=99:
                rn = view[1:]
                if len(vacated) == 0:
                    car_dictionary[i] = rn
                    val = 'Slot no. {} alloted!'.format(i)
                    i+=1
                    print(car_dictionary)
                    return jsonify({'name': val})
                else:
                    vacated.sort()
                    first = vacated[0]
                    car_dictionary[first] = rn
                    val = 'Slot no. {} alloted!'.format(first)
                    vacated.pop(0)
                    print(car_dictionary)
                    print(vacated)
                    return jsonify({'name': val})
        elif text == 'leave' or text == 'Leave':
            num = int(view[1])
            if num > len(car_dictionary):
                stat = "Please fill the slot to vacate"
                return jsonify({'name': stat})
            else:
                car_dictionary[num] = ''
                leave = 'Slot no. {} vacated & the charge is {} INR.!'.format(view[1],'30')
                vacated.append(num)
                print(car_dictionary)
                print(vacated)
                return jsonify({'name': leave})
        else:
            return jsonify({'name': 'Wrong Input'})
    else:
        return jsonify({'name': 'Wrong Input'})

if __name__ == "__main__":
    app.run(debug=True)