#!/bin/bash

# Record the marketplace demo and create a GIF

echo "🎬 Recording Marketplace Demo..."
echo ""
echo "This will:"
echo "1. Record the demo with asciinema"
echo "2. Convert to GIF"
echo "3. Save as demo.gif"
echo ""
echo "Starting in 3 seconds..."
sleep 3

# Record the demo
asciinema rec demo.cast -c "python3 demo_standalone.py" --overwrite

# Convert to GIF
echo ""
echo "Converting to GIF..."
agg demo.cast demo.gif --speed 2 --font-size 14

echo ""
echo "✅ Done! Created:"
echo "   - demo.cast (terminal recording)"
echo "   - demo.gif (animated GIF)"
echo ""
echo "Upload demo.gif to your README!"
