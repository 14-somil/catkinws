;; Auto-generated. Do not edit!


(when (boundp 'beginner_tutorials::encodersFeedback)
  (if (not (find-package "BEGINNER_TUTORIALS"))
    (make-package "BEGINNER_TUTORIALS"))
  (shadow 'encodersFeedback (find-package "BEGINNER_TUTORIALS")))
(unless (find-package "BEGINNER_TUTORIALS::ENCODERSFEEDBACK")
  (make-package "BEGINNER_TUTORIALS::ENCODERSFEEDBACK"))

(in-package "ROS")
;;//! \htmlinclude encodersFeedback.msg.html


(defclass beginner_tutorials::encodersFeedback
  :super ros::object
  :slots (_first _second _base ))

(defmethod beginner_tutorials::encodersFeedback
  (:init
   (&key
    ((:first __first) 0.0)
    ((:second __second) 0.0)
    ((:base __base) 0.0)
    )
   (send-super :init)
   (setq _first (float __first))
   (setq _second (float __second))
   (setq _base (float __base))
   self)
  (:first
   (&optional __first)
   (if __first (setq _first __first)) _first)
  (:second
   (&optional __second)
   (if __second (setq _second __second)) _second)
  (:base
   (&optional __base)
   (if __base (setq _base __base)) _base)
  (:serialization-length
   ()
   (+
    ;; float64 _first
    8
    ;; float64 _second
    8
    ;; float64 _base
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
     ;; float64 _base
       (sys::poke _base (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _first
     (setq _first (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _second
     (setq _second (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _base
     (setq _base (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get beginner_tutorials::encodersFeedback :md5sum-) "0745d61b2a4b159f25fc57eee55861a2")
(setf (get beginner_tutorials::encodersFeedback :datatype-) "beginner_tutorials/encodersFeedback")
(setf (get beginner_tutorials::encodersFeedback :definition-)
      "float64 first
float64 second
float64 base
")



(provide :beginner_tutorials/encodersFeedback "0745d61b2a4b159f25fc57eee55861a2")


