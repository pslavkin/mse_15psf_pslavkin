DRY= #--dry-run
rclone sync --verbose --progress --copy-links \
   $DRY\
   --exclude=*.jpg \
   --exclude=*.png \
   --exclude=*.bin \
   --exclude=*.o \
   --exclude=*.d \
   --exclude=*.mp4 \
   --exclude=*.swp \
   --exclude=*.hex \
   --exclude=*.lst \
   --exclude=*.elf \
   --exclude=*.a \
   --exclude=*.csv \
   --exclude=*.map \
   --exclude=rclone* \
   --exclude=*.zip \
   --exclude=*__pycache__/ \
   --exclude=kicad\** \
   --delete-excluded \
   .\
   capse:"FI-UBA MSE/PSF/clases" 
