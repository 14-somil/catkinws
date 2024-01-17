// Generated by gencpp from file final_rover/anglesMsg.msg
// DO NOT EDIT!


#ifndef FINAL_ROVER_MESSAGE_ANGLESMSG_H
#define FINAL_ROVER_MESSAGE_ANGLESMSG_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace final_rover
{
template <class ContainerAllocator>
struct anglesMsg_
{
  typedef anglesMsg_<ContainerAllocator> Type;

  anglesMsg_()
    : y(0.0)
    , first(0.0)
    , second(0.0)
    , pitch(0.0)
    , yaw(0.0)
    , gripper(0)  {
    }
  anglesMsg_(const ContainerAllocator& _alloc)
    : y(0.0)
    , first(0.0)
    , second(0.0)
    , pitch(0.0)
    , yaw(0.0)
    , gripper(0)  {
  (void)_alloc;
    }



   typedef double _y_type;
  _y_type y;

   typedef double _first_type;
  _first_type first;

   typedef double _second_type;
  _second_type second;

   typedef double _pitch_type;
  _pitch_type pitch;

   typedef double _yaw_type;
  _yaw_type yaw;

   typedef int16_t _gripper_type;
  _gripper_type gripper;





  typedef boost::shared_ptr< ::final_rover::anglesMsg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::final_rover::anglesMsg_<ContainerAllocator> const> ConstPtr;

}; // struct anglesMsg_

typedef ::final_rover::anglesMsg_<std::allocator<void> > anglesMsg;

typedef boost::shared_ptr< ::final_rover::anglesMsg > anglesMsgPtr;
typedef boost::shared_ptr< ::final_rover::anglesMsg const> anglesMsgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::final_rover::anglesMsg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::final_rover::anglesMsg_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::final_rover::anglesMsg_<ContainerAllocator1> & lhs, const ::final_rover::anglesMsg_<ContainerAllocator2> & rhs)
{
  return lhs.y == rhs.y &&
    lhs.first == rhs.first &&
    lhs.second == rhs.second &&
    lhs.pitch == rhs.pitch &&
    lhs.yaw == rhs.yaw &&
    lhs.gripper == rhs.gripper;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::final_rover::anglesMsg_<ContainerAllocator1> & lhs, const ::final_rover::anglesMsg_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace final_rover

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::final_rover::anglesMsg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::final_rover::anglesMsg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::final_rover::anglesMsg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::final_rover::anglesMsg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::final_rover::anglesMsg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::final_rover::anglesMsg_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::final_rover::anglesMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4129c29ab0d655cecd752c50ae83f843";
  }

  static const char* value(const ::final_rover::anglesMsg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4129c29ab0d655ceULL;
  static const uint64_t static_value2 = 0xcd752c50ae83f843ULL;
};

template<class ContainerAllocator>
struct DataType< ::final_rover::anglesMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "final_rover/anglesMsg";
  }

  static const char* value(const ::final_rover::anglesMsg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::final_rover::anglesMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 y\n"
"float64 first\n"
"float64 second\n"
"float64 pitch\n"
"float64 yaw\n"
"int16 gripper\n"
;
  }

  static const char* value(const ::final_rover::anglesMsg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::final_rover::anglesMsg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.y);
      stream.next(m.first);
      stream.next(m.second);
      stream.next(m.pitch);
      stream.next(m.yaw);
      stream.next(m.gripper);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct anglesMsg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::final_rover::anglesMsg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::final_rover::anglesMsg_<ContainerAllocator>& v)
  {
    s << indent << "y: ";
    Printer<double>::stream(s, indent + "  ", v.y);
    s << indent << "first: ";
    Printer<double>::stream(s, indent + "  ", v.first);
    s << indent << "second: ";
    Printer<double>::stream(s, indent + "  ", v.second);
    s << indent << "pitch: ";
    Printer<double>::stream(s, indent + "  ", v.pitch);
    s << indent << "yaw: ";
    Printer<double>::stream(s, indent + "  ", v.yaw);
    s << indent << "gripper: ";
    Printer<int16_t>::stream(s, indent + "  ", v.gripper);
  }
};

} // namespace message_operations
} // namespace ros

#endif // FINAL_ROVER_MESSAGE_ANGLESMSG_H
