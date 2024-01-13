// Generated by gencpp from file beginner_tutorials/anglesMsg.msg
// DO NOT EDIT!


#ifndef BEGINNER_TUTORIALS_MESSAGE_ANGLESMSG_H
#define BEGINNER_TUTORIALS_MESSAGE_ANGLESMSG_H


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
struct anglesMsg_
{
  typedef anglesMsg_<ContainerAllocator> Type;

  anglesMsg_()
    : first(0.0)
    , second(0.0)
    , base(0.0)
    , servo1(0)
    , servo2(0)
    , servo3(0)
    , isPump(false)  {
    }
  anglesMsg_(const ContainerAllocator& _alloc)
    : first(0.0)
    , second(0.0)
    , base(0.0)
    , servo1(0)
    , servo2(0)
    , servo3(0)
    , isPump(false)  {
  (void)_alloc;
    }



   typedef double _first_type;
  _first_type first;

   typedef double _second_type;
  _second_type second;

   typedef double _base_type;
  _base_type base;

   typedef int64_t _servo1_type;
  _servo1_type servo1;

   typedef int64_t _servo2_type;
  _servo2_type servo2;

   typedef int64_t _servo3_type;
  _servo3_type servo3;

   typedef uint8_t _isPump_type;
  _isPump_type isPump;





  typedef boost::shared_ptr< ::beginner_tutorials::anglesMsg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::beginner_tutorials::anglesMsg_<ContainerAllocator> const> ConstPtr;

}; // struct anglesMsg_

typedef ::beginner_tutorials::anglesMsg_<std::allocator<void> > anglesMsg;

typedef boost::shared_ptr< ::beginner_tutorials::anglesMsg > anglesMsgPtr;
typedef boost::shared_ptr< ::beginner_tutorials::anglesMsg const> anglesMsgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::beginner_tutorials::anglesMsg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::beginner_tutorials::anglesMsg_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::beginner_tutorials::anglesMsg_<ContainerAllocator1> & lhs, const ::beginner_tutorials::anglesMsg_<ContainerAllocator2> & rhs)
{
  return lhs.first == rhs.first &&
    lhs.second == rhs.second &&
    lhs.base == rhs.base &&
    lhs.servo1 == rhs.servo1 &&
    lhs.servo2 == rhs.servo2 &&
    lhs.servo3 == rhs.servo3 &&
    lhs.isPump == rhs.isPump;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::beginner_tutorials::anglesMsg_<ContainerAllocator1> & lhs, const ::beginner_tutorials::anglesMsg_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace beginner_tutorials

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::beginner_tutorials::anglesMsg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::beginner_tutorials::anglesMsg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::beginner_tutorials::anglesMsg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::beginner_tutorials::anglesMsg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::beginner_tutorials::anglesMsg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::beginner_tutorials::anglesMsg_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::beginner_tutorials::anglesMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6b8e0d4ccdce3065f67c69afb3a3bac4";
  }

  static const char* value(const ::beginner_tutorials::anglesMsg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6b8e0d4ccdce3065ULL;
  static const uint64_t static_value2 = 0xf67c69afb3a3bac4ULL;
};

template<class ContainerAllocator>
struct DataType< ::beginner_tutorials::anglesMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "beginner_tutorials/anglesMsg";
  }

  static const char* value(const ::beginner_tutorials::anglesMsg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::beginner_tutorials::anglesMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 first\n"
"float64 second\n"
"float64 base\n"
"int64 servo1 \n"
"int64 servo2\n"
"int64 servo3\n"
"bool isPump\n"
;
  }

  static const char* value(const ::beginner_tutorials::anglesMsg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::beginner_tutorials::anglesMsg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.first);
      stream.next(m.second);
      stream.next(m.base);
      stream.next(m.servo1);
      stream.next(m.servo2);
      stream.next(m.servo3);
      stream.next(m.isPump);
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
struct Printer< ::beginner_tutorials::anglesMsg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::beginner_tutorials::anglesMsg_<ContainerAllocator>& v)
  {
    s << indent << "first: ";
    Printer<double>::stream(s, indent + "  ", v.first);
    s << indent << "second: ";
    Printer<double>::stream(s, indent + "  ", v.second);
    s << indent << "base: ";
    Printer<double>::stream(s, indent + "  ", v.base);
    s << indent << "servo1: ";
    Printer<int64_t>::stream(s, indent + "  ", v.servo1);
    s << indent << "servo2: ";
    Printer<int64_t>::stream(s, indent + "  ", v.servo2);
    s << indent << "servo3: ";
    Printer<int64_t>::stream(s, indent + "  ", v.servo3);
    s << indent << "isPump: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.isPump);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BEGINNER_TUTORIALS_MESSAGE_ANGLESMSG_H
