// Generated by gencpp from file beginner_tutorials/speedMsg.msg
// DO NOT EDIT!


#ifndef BEGINNER_TUTORIALS_MESSAGE_SPEEDMSG_H
#define BEGINNER_TUTORIALS_MESSAGE_SPEEDMSG_H


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
struct speedMsg_
{
  typedef speedMsg_<ContainerAllocator> Type;

  speedMsg_()
    : first(0.0)
    , second(0.0)
    , base(0.0)  {
    }
  speedMsg_(const ContainerAllocator& _alloc)
    : first(0.0)
    , second(0.0)
    , base(0.0)  {
  (void)_alloc;
    }



   typedef double _first_type;
  _first_type first;

   typedef double _second_type;
  _second_type second;

   typedef double _base_type;
  _base_type base;





  typedef boost::shared_ptr< ::beginner_tutorials::speedMsg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::beginner_tutorials::speedMsg_<ContainerAllocator> const> ConstPtr;

}; // struct speedMsg_

typedef ::beginner_tutorials::speedMsg_<std::allocator<void> > speedMsg;

typedef boost::shared_ptr< ::beginner_tutorials::speedMsg > speedMsgPtr;
typedef boost::shared_ptr< ::beginner_tutorials::speedMsg const> speedMsgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::beginner_tutorials::speedMsg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::beginner_tutorials::speedMsg_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::beginner_tutorials::speedMsg_<ContainerAllocator1> & lhs, const ::beginner_tutorials::speedMsg_<ContainerAllocator2> & rhs)
{
  return lhs.first == rhs.first &&
    lhs.second == rhs.second &&
    lhs.base == rhs.base;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::beginner_tutorials::speedMsg_<ContainerAllocator1> & lhs, const ::beginner_tutorials::speedMsg_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace beginner_tutorials

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::beginner_tutorials::speedMsg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::beginner_tutorials::speedMsg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::beginner_tutorials::speedMsg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::beginner_tutorials::speedMsg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::beginner_tutorials::speedMsg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::beginner_tutorials::speedMsg_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::beginner_tutorials::speedMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "0745d61b2a4b159f25fc57eee55861a2";
  }

  static const char* value(const ::beginner_tutorials::speedMsg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x0745d61b2a4b159fULL;
  static const uint64_t static_value2 = 0x25fc57eee55861a2ULL;
};

template<class ContainerAllocator>
struct DataType< ::beginner_tutorials::speedMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "beginner_tutorials/speedMsg";
  }

  static const char* value(const ::beginner_tutorials::speedMsg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::beginner_tutorials::speedMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 first\n"
"float64 second\n"
"float64 base\n"
;
  }

  static const char* value(const ::beginner_tutorials::speedMsg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::beginner_tutorials::speedMsg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.first);
      stream.next(m.second);
      stream.next(m.base);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct speedMsg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::beginner_tutorials::speedMsg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::beginner_tutorials::speedMsg_<ContainerAllocator>& v)
  {
    s << indent << "first: ";
    Printer<double>::stream(s, indent + "  ", v.first);
    s << indent << "second: ";
    Printer<double>::stream(s, indent + "  ", v.second);
    s << indent << "base: ";
    Printer<double>::stream(s, indent + "  ", v.base);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BEGINNER_TUTORIALS_MESSAGE_SPEEDMSG_H
