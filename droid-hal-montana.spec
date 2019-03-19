# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device montana
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty Moto G5S

%define installable_zip 1

%define straggler_files \
/bugreports\
/d\
/file_contexts.bin\
/init.class_main.sh\
/init.mmi.audio.sh\
/init.mmi.block_perm.sh\
/init.mmi.boot.sh\
/init.mmi.laser.sh\
/init.mmi.usb.sh\
/init.oem.hw.sh\
/init.qcom.class_core.sh\
/init.qcom.early_boot.sh\
/init.qcom.sensors.sh\
/init.qcom.sh\
/init.qcom.syspart_fixup.sh\
/property_contexts\
/sdcard\
/selinux_version\
/service_contexts\
/vendor\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

