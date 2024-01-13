// Generated by gencpp from file beginner_tutorials/RoverMsg.msg
// DO NOT EDIT!


#ifndef BEGINNER_TUTORIALS_MESSAGE_ROVERMSG_H
#define BEGINNER_TUTORIALS_MESSAGE_ROVERMSG_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace beginner_tutorials
{
template <class ContainerAllocator>
struct RoverMsg_
{
  typedef RoverMsg_<ContainerAllocator> Type;

  RoverMsg_()
    : x(0.0)
    , y(0.0)  {
    }
  RoverMsg_(const ContainerAllocator& _alloc)
    : x(0.0)
    , y(0.0)  {
  (void)_alloc;
    }



   typedef double _x_type;
  _x_type x;

   typedef double _y_type;
  _y_type y;





  typedef boost::shared_ptr< ::beginner_tutorials::RoverMsg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::beginner_tutorials::RoverMsg_<ContainerAllocator> const> ConstPtr;

}; // struct RoverMsg_

typedef ::beginner_tutorials::RoverMsg_<std::allocator<void> > RoverMsg;

typedef boost::shared_ptr< ::beginner_tutorials::RoverMsg > RoverMsgPtr;
typedef boost::shared_ptr< ::beginner_tutorials::RoverMsg const> RoverMsgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::beginner_tutorials::RoverMsg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::beginner_tutorials::RoverMsg_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::beginner_tutorials::RoverMsg_<ContainerAllocator1> & lhs, const ::beginner_tutorials::RoverMsg_<ContainerAllocator2> & rhs)
{
  return lhs.x == rhs.x &&
    lhs.y == rhs.y;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::beginner_tutorials::RoverMsg_<ContainerAllocator1> & lhs, const ::beginner_tutorials::RoverMsg_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace beginner_tutorials

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::beginner_tutorials::RoverMsg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::beginner_tutorials::RoverMsg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::beginner_tutorials::RoverMsg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::beginner_tutorials::RoverMsg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::beginner_tutorials::RoverMsg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::beginner_tutorials::RoverMsg_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::beginner_tutorials::RoverMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "209f516d3eb691f0663e25cb750d67c1";
  }

  static const char* value(const ::beginner_tutorials::RoverMsg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x209f516d3eb691f0ULL;
  static const uint64_t static_value2 = 0x663e25cb750d67c1ULL;
};

template<class ContainerAllocator>
struct DataType< ::beginner_tutorials::RoverMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "beginner_tutorials/RoverMsg";
  }

  static const char* value(const ::beginner_tutorials::RoverMsg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::beginner_tutorials::RoverMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 x\n"
"float64 y\n"
;
  }

  static const char* value(const ::beginner_tutorials::RoverMsg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::beginner_tutorials::RoverMsg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RoverMsg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::beginner_tutorials::RoverMsg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::beginner_tutorials::RoverMsg_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<double>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<double>::stream(s, indent + "  ", v.y);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BEGINNER_TUTORIALS_MESSAGE_ROVERMSG_H
