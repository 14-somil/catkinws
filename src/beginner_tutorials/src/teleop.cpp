#include <iostream>
#include "ros/ros.h"
#include "std_msgs/Char.h"
#include <conio.h>

using namespace std;

int main(int argc, char **argv)
{
    ros::init(argc, argv, "teleop");
    ros::NodeHandle n;

    ros::Publisher pub=n.advertise<std_msgs::Char>("/cmd_vel", 10);
    ros::Rate loop_rate(1);

    cout<<"Press x to exit\n";

    while(ros::ok())
    {
        std_msgs::Char msg;
        char a=getch();
        if(a=='x' || a==3)
        {
            break;
        }
        msg.data = a;
        cout<<a<<endl;
        pub.publish(msg);

        ros::spinOnce();

        loop_rate.sleep();
    }


    return 0;
}