;; Auto-generated. Do not edit!


(when (boundp 'beginner_tutorials::encodersFeedback)
  (if (not (find-package "BEGINNER_TUTORIALS"))
    (make-package "BEGINNER_TUTORIALS"))
  (shadow 'encodersFeedback (find-package "BEGINNER_TUTORIALS")))
(unless (find-package "BEGINNER_TUTORIALS::ENCODERSFEEDBACK")
  (make-package "BEGINNER_TUTORIALS::ENCODERSFEEDBACK"))

(in-package "ROS")
;;//! \htmlinclude encodersFeedback.msg.html


(intern "*BASE*" (find-package "BEGINNER_TUTORIALS::ENCODERSFEEDBACK"))
(shadow '*BASE* (find-package "BEGINNER_TUTORIALS::ENCODERSFEEDBACK"))
(defconstant beginner_tutorials::encodersFeedback::*BASE* 0.0)

(defun beginner_tutorials::encodersFeedback-to-symbol (const)
  (cond
        (t nil)))

(defclass beginner_tutorials::encodersFeedback
  :super ros::object
  :slots (_first _second ))

(defmethod beginner_tutorials::encodersFeedback
  (:init
   (&key
    ((:first __first) 0.0)
    ((:second __second) 0.0)
    )
   (send-super :init)
   (setq _first (float __first))
   (setq _second (float __second))
   self)
  (:first
   (&optional __first)
   (if __first (setq _first __first)) _first)
  (:second
   (&optional __second)
   (if __second (setq _second __second)) _second)
  (:serialization-length
   ()
   (+
    ;; float64 _first
    8
    ;; float64 _second
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _first
       (sys::poke _first (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _second
       (sys::poke _second (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _first
     (setq _first (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _second
     (setq _second (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get beginner_tutorials::encodersFeedback :md5sum-) "7506f42907eb3eaefadf3e0d4485e175")
(setf (get beginner_tutorials::encodersFeedback :datatype-) "beginner_tutorials/encodersFeedback")
(setf (get beginner_tutorials::encodersFeedback :definition-)
      "float64 first
float64 second
float64 base=0
")



(provide :beginner_tutorials/encodersFeedback "7506f42907eb3eaefadf3e0d4485e175")


