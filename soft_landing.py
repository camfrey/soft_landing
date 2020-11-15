import matplotlib
from matplotlib import pyplot as plt
import math
#------------------------------------------------
GRAVITY=1.622# assumed to be m/s**2. This is the gravity of the moon
POWER = 4.0 # This is the amount of thrust received for each unit of fuel expended.
STRENGTH_INIT = 4 # The lander's strength (won't change in this program).
FUEL_INIT=20
landing_attempt=0


def get_manual_or_automatic():
    '''
     Sets the game to manual or automatic
    no parameters
    returns
        m for manual or a for automatic 
    '''
    response=input("Manual or automatic, type m or a:")
    conditional=True
    while conditional==True:
        if response == "a" or response =="A":
            mode = "a"
            conditional=False
        elif response =="m" or response == "M":
            mode = "m"
            conditional=False
        else:
             response=input("Manual or automatic, type m or a:")
    return mode


#-------------------------------------------------

def show_status(altitude,speed,fuel,strength):
    '''
    Prints the status of altitude speed fuel and strength
    Paramters
        altitude(float)- the height above ground 
        speed(float)- how fast the ship is traveling
        fuel(int)- amount of fuel left
        stregnth(int)- ship's strength
    returns
        prints all numbers passed to it 
    '''
    
    print('Alt=',altitude,'Vel=',speed,'Fuel=',fuel,'Str=',strength)

#---------------------------------------------------

def get_thrust_from_user(altitude,speed,fuel,strength):
    '''
    Asks user to enter a thrust value
    paramaters
        altitude(float)- the height above ground 
        speed(float)- how fast the ship is traveling
        fuel(int)- amount of fuel left
        stregnth(int)- ship's strength
    returns
        gives back the thrust value entered
    '''
    thrust = input('Enter a thrust value:')
    conditional=True 
    while conditional==True:
        if thrust == '':
            thrust = input('Enter a thrust value:')
        elif int(thrust) > fuel:
            thrust = input('Enter a thrust value:')
        elif int(thrust)<0:
            thrust = input('Enter a thrust value:')
        elif int(thrust)>strength:
             thrust = input('Enter a thrust value:')
        else:
            conditional = False
    return int(thrust)


#--------------------------------------------------
def apply_thrut(thrust,fuel,strength,speed):
    '''
     Calculates the change in speed and the fuel used 
     Parameters 
        Thrust(int)- thrust applied away from the ground
        fuel(int)- amount of fuel left
        stregnth(int)- ship's strength
        speed(float)- the current speed of the lander
    returns
        speed(float)- the new speed of the lander after thrust is applied
        fuel(int)- the new fuel left in the lander
    '''
    
    speed= speed - thrust * strength
    fuel=fuel - thrust
    return speed,fuel
#------------------------------------------------
    
def update_one_second(altitude,speed):
    '''
    Updates the altitude and applies the acceleration of gravity
    Parameters
        altitude(float)- the current altitude of the lander
        speed(float)- the speed before gravity
    returns
        altitude(float)- new altitude 
        speed(float)- new speed
    '''
    speed= speed +GRAVITY
    altitude= altitude-speed
    if altitude <=0:
        altitude= 0
    return altitude,speed 

#-----------------------------------

def report_landing(speed,strength):
    '''
     reports wether the ship lands or not
    Parameters
        speed(float)- the speed of the of the lander
        strength(int)- the strength of the lander
    returns
        True or False
    '''
    if speed<=strength and speed>=0:
        return True
    else:
        return False

#---------------------------------------

def solve_kinematics(altitude,speed):
    '''
    Computes the time it would take for the lander at the given altitude
        and speed to land if no thrust were applied; computes the speed 
        at landing if no thrust were applied
    Paramters:
        altitude: (float) - current altitude of lander
        speed: (float) - current speed of lander
    Returns:
        time, landing_speed: both floats 
    '''
    
    # kinematic equation     
    # (GRAVITY/2)*time**2 + speed*time - altitude = 0
    
    # solve quadratic equation for time using discriminant
    a = (GRAVITY/2)
    b = speed
    c = -altitude
    discriminant = (b**2 - 4*a*c)
         
    #time represents the number of iterations left in
    #simulation if there was no thrust
    time = (-b + math.sqrt(discriminant))/(2*a)
    
    #speed that the ship would land if no thrust applied   
    landing_speed = speed + (GRAVITY*math.ceil(time))
    
    return time,landing_speed
#------------------------------------------------------------------------   
    
def auto_generate_thrust(altitude,speed,fuel,strength):
    '''
    Generates a thrsut value off of the current stats of the ship
    Parameters
        altitude(float)- the height above ground 
        speed(float)- how fast the ship is traveling
        fuel(int)- amount of fuel left
        stregnth(int)- ship's strength
    Returns
        thrust(int)- thrust applied to ship
    '''
    # initialize thrust
    thrust = 0
    
    # compute the time and landing speed 
    # the time represents how many iterations of the simulation would be left
    # if no thrust were applied and the theor_landing_speed is a prediction of
    # the velocity of the ship at landing if no thrust were applied
    
    num_iteration_left,theor_landing_speed = solve_kinematics(altitude,speed)
    
    # Your job is to compute how much thrust to apply based on:
    # the number of iterations of the simuation left 
    # the speed at which the ship would land 
    # the amount of fuel left
   
    
    # Your code goes here
    if theor_landing_speed>10:
        if num_iteration_left<4:
            thrust=4
    
    elif theor_landing_speed>20:
        if num_iteration_left<4:
            thrust=4
    
    elif theor_landing_speed>30:
        if num_iteration_left<4:
            thrust=4
    
    elif theor_landing_speed>40:
        if num_iteration_left<4:
            thrust=4
    
    elif theor_landing_speed>50:
        if num_iteration_left<4:
            thrust=4
    
    elif theor_landing_speed>60:
        if num_iteration_left<4:
            thrust=4
    
    if thrust>fuel:
        thrust=fuel
    
    elif thrust>strength:
        thrust=strength 

    return thrust
    
#---------------------------------------------------------------
def get_integer(maximum,prompt):
    '''
    Asks the user to enter an integer 
    Parameters
        maximum(int)- the maximum value of the integer
        prompt(str)- prompt displayed when user is asked for integer
    returns
        num(int)- valid inputed value
    '''
    con=True
    while con==True:
        num=input(prompt)
        if num.isdigit()==True:
            if int(num)<=maximum:
                con=False
                return int(num)
            elif maximum<0:
                con=False
                return int(num)



#-----------------------------------------

def is_float(s):
    '''
    Determins if a number is a float or not
    Paramaters
        s(string)- value to be evaluated
    returns
        True or False
    '''
    try:
        float(s)
        return True
    except ValueError:
        return False

#-------------------------------------

def get_float(prompt):
    '''
    Gets a float number from the user
    Parameters
        prompt(str)- prompt displayed to user
    returns
        prompt(float)- a valid inputed float
    '''
    con=False
    while con==False:
        if is_float(prompt)==True:
            con=True
            return float(prompt)
        else:
            prompt=input('Enter a float value:')

#print(get_float('-.1'))
#-------------------------------------

def get_history_filename(landing_num):
    '''
    Gets the number for a file
    Parameters
        landing_num(int)- number marking file
    returns
        LandingNN.csv
    '''
    if landing_num>=0 and landing_num<10:
        land_num='0'+str(landing_num)
    else:
        land_num=str(landing_num)
    return 'Landing'+land_num+'.csv'


#------------------------------------

def get_initial_conditions():
    '''
    Asks the user to enter the initial conditions 
    Paramters
        none
    returns
        the initial conditions 
    '''
    con=True
    while con==True:
        prompt_A=input('Enter the altitude:')
        altitude=get_float(prompt_A)
        if altitude >=0:
            con=False

    
    promt_S=input('Enter the speed:')
    speed=get_float(promt_S)
    
    
    fuel=get_integer(100,'Enter a fuel:')
    
    
    return [altitude,speed,fuel]


#print(get_initial_conditions())

#------------------------------------

def save_history(history_list,landing_num):
    '''
    Takes a file and writes to it organzing data of the landing data
    Parameters
        history_list(list)- data to be organized 
        landing_num(int)- number assigned to file
    returns
        none
    '''
    
    file=get_history_filename(landing_num)
    history=open(file,'w')
    history.write(str(len(history_list))+'\n')
    for alist in history_list:
        string=''
        for num in alist:
            string+=str(num) + ','
        string=string.strip(',')
        string+='\n'
        history.write(string)
    history.close()
    
history =[ [3.61, 2.98, 15],  [3.01, 0.6, 14],  [0.79, 2.22, 14],  [0, 3.84, 14]]

    

#------------------------------------

def get_response(valid_entries,prompt):
    '''
    Asks user to enter a valid entry
    Parameters
        valid_entries(str)- valid entries
        prompt(str)- prompt displayed to user
    returns
        char(str)-valid entry 
    '''
    while True:
        char=input(prompt)
        for element in valid_entries:
            if char== element or char.swapcase()==element:
                return char.lower()

#---------------------------------------

def plot_history(history_list):
    '''
    '''
    fig, his =plt.subplots()
    count=0
    alt_x_values=[]
    alt_y_values=[]
    speed_x_values=[]
    speed_y_values=[]
    fuel_x_values=[]
    fuel_y_values=[]
    for list in history_list:
        alt_x_values.append(count)
        speed_x_values.append(count)
        fuel_x_values.append(count)
        count+=1
        alt_y_values.append(list[0])
        speed_y_values.append(list[1])
        fuel_y_values.append(list[2])
    his.plot(alt_x_values,alt_y_values,color='b',marker='s',label='altitude m')
    his.plot(speed_x_values,speed_y_values,color='g',marker='o',label='speed m/s')
    his.plot(fuel_x_values,fuel_y_values,color='r',marker='*',label='fuel units')
    plt.title('Lander Simulation')
    plt.xlabel('Time - seconds')
    his.legend()
    plt.show()
    fig.show()



#-----------------------------------------------------------------
def main():
    '''
    Runs the entire land ship program
    No parameters
    Returns 
        Prints success or crash
    '''
    landing_attempt=1
    
    answer='a'
    
    strength=STRENGTH_INIT
    while answer!='q':
        lander_data=[]
        conditions= get_initial_conditions()
        altitude=conditions[0]
        speed=conditions[1]
        fuel=conditions[2]
        conditions.append(0)
        lander_data.append(conditions)
        
        mode=get_manual_or_automatic() #Aks user to set program to manual or automatic
    
        show_status(conditions[0],conditions[1],conditions[2],strength)    #Display the starting conditions
    
        if mode == "m":
            while altitude>0 and fuel>0:
                
                thrust= get_thrust_from_user(altitude,speed,fuel,strength)
                #Gets a thrust value from the user 
                
                speed,fuel= apply_thrut(thrust,fuel,strength,speed)
                 #Calculates the speed change and fuel used by lander
                 
                altitude,speed= update_one_second(altitude,speed)
                #Calculates the new altitude of the lander 
                  
                show_status(altitude,speed,fuel,strength)
                #Displays the conditions of the lander 
                
                lander_data.append([altitude,speed,fuel,thrust])
                
            if report_landing(speed,strength)==True:
                print('success')
            
            elif altitude <=0 or fuel<=0:
                print('crash')
                #Prints whether the lander crashed or landed succesfully 
            
            save_history(lander_data,landing_attempt)
            
            answer= get_response('qap','Enter q to quit, a to try again, or p to plot:')
            
            if answer=='p':
                while answer=='p':
                    plot_history(lander_data)
                    answer= get_response('qap','Enter q to quit, a to try again, or p to plot:')
            if answer=='a':
                landing_attempt+=1
    
     
        elif mode == 'a':
            
            while altitude>0 and fuel>0:
                
                thrust=auto_generate_thrust(altitude,speed,fuel,strength)
                
                print(thrust)
                
                speed,fuel= apply_thrut(thrust,fuel,strength,speed)
                
                
                altitude,speed= update_one_second(altitude,speed)
                
                
                show_status(altitude,speed,fuel,strength)
                
                lander_data.append([altitude,speed,fuel,thrust])
                
            if report_landing(speed,strength)==True:
                print('success')
            
            elif altitude <=0 or fuel<=0:
                print('crash')
            
            save_history(lander_data,landing_attempt)
            
            answer= get_response('qap','Enter q to quit, a to try again, or p to plot:')
            
            if answer=='p':
                while answer=='p':
                    plot_history(lander_data)
                    answer= get_response('qap','Enter q to quit, a to try again, or p to plot:')
            if answer=='a':
                landing_attempt+=1


main()