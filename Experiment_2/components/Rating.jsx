import { useState } from 'react';
import Rating from '@mui/material/Rating';
import Box from '@mui/material/Box';
import StarIcon from '@mui/icons-material/Star';

export default function RatingComponent() {
  const [value, setValue] = useState(2);

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
      <div>
        <h3>Basic Rating</h3>
        <Rating 
          value={value} 
          onChange={(event, newValue) => {
            setValue(newValue);
          }} 
        />
      </div>
      
      <div>
        <h3>Read-only Rating</h3>
        <Rating value={4} readOnly />
      </div>

      <div>
        <h3>Custom Icon Rating</h3>
        <Rating 
          icon={<StarIcon fontSize="inherit" />}
          emptyIcon={<StarIcon fontSize="inherit" />}
          value={3}
        />
      </div>
    </Box>
  );
}
