;; Auto-generated. Do not edit!


(when (boundp 'beginner_tutorials::roboticArmController)
  (if (not (find-package "BEGINNER_TUTORIALS"))
    (make-package "BEGINNER_TUTORIALS"))
  (shadow 'roboticArmController (find-package "BEGINNER_TUTORIALS")))
(unless (find-package "BEGINNER_TUTORIALS::ROBOTICARMCONTROLLER")
  (make-package "BEGINNER_TUTORIALS::ROBOTICARMCONTROLLER"))

(in-package "ROS")
;;//! \htmlinclude roboticArmController.msg.html


(defclass beginner_tutorials::roboticArmController
  :super ros::object
  :slots (_y _first _second _pitch _yaw _gripper ))

(defmethod beginner_tutorials::roboticArmController
  (:init
   (&key
    ((:y __y) 0.0)
    ((:first __first) 0.0)
    ((:second __second) 0.0)
    ((:pitch __pitch) 0.0)
    ((:yaw __yaw) 0.0)
    ((:gripper __gripper) 0)
    )
   (send-super :init)
   (setq _y (float __y))
   (setq _first (float __first))
   (setq _second (float __second))
   (setq _pitch (float __pitch))
   (setq _yaw (float __yaw))
   (setq _gripper (round __gripper))
   self)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:first
   (&optional __first)
   (if __first (setq _first __first)) _first)
  (:second
   (&optional __second)
   (if __second (setq _second __second)) _second)
  (:pitch
   (&optional __pitch)
   (if __pitch (setq _pitch __pitch)) _pitch)
  (:yaw
   (&optional __yaw)
   (if __yaw (setq _yaw __yaw)) _yaw)
  (:gripper
   (&optional __gripper)
   (if __gripper (setq _gripper __gripper)) _gripper)
  (:serialization-length
   ()
   (+
    ;; float64 _y
    8
    ;; float64 _first
    8
    ;; float64 _second
    8
    ;; float64 _pitch
    8
    ;; float64 _yaw
    8
    ;; int16 _gripper
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _first
       (sys::poke _first (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _second
       (sys::poke _second (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _pitch
       (sys::poke _pitch (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _yaw
       (sys::poke _yaw (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; int16 _gripper
       (write-word _gripper s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _first
     (setq _first (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _second
     (setq _second (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _pitch
     (setq _pitch (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _yaw
     (setq _yaw (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; int16 _gripper
     (setq _gripper (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get beginner_tutorials::roboticArmController :md5sum-) "4129c29ab0d655cecd752c50ae83f843")
(setf (get beginner_tutorials::roboticArmController :datatype-) "beginner_tutorials/roboticArmController")
(setf (get beginner_tutorials::roboticArmController :definition-)
      "float64 y
float64 first
float64 second
float64 pitch
float64 yaw
int16 gripper
")



(provide :beginner_tutorials/roboticArmController "4129c29ab0d655cecd752c50ae83f843")


