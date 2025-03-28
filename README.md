# Worthing SW API
## API

### /profiles

`GET` : Get all profiles
<details> 
<summary> Typical GET response </summary>

	```
	{
	  "count": 2,
	  "next": null,
	  "previous": null,
	  "results": [
	    {
	      "id": 2,
	      "user": "gooobles",
	      "bio": "",
	      "created_at": "12 Mar 2025",
	      "image": "https://res.cloudinary.com/dt7dd37h8/image/upload/v1/media/../guitar-logo-white_utocxc",
	      "is_user": false,
	      "following_id": null,
	      "following_count": 0,
	      "followers_count": 0,
	      "posts_count": 1
	    },
	    {
	      "id": 1,
	      "user": "differi",
	      "bio": "",
	      "created_at": "12 Mar 2025",
	      "image": "https://res.cloudinary.com/dt7dd37h8/image/upload/v1/media/../guitar-logo-white_utocxc",
	      "is_user": false,
	      "following_id": null,
	      "following_count": 0,
	      "followers_count": 0,
	      "posts_count": 3
	    }
	  ]
	}
	```

</details>

### /profiles/:id

`GET` : Get a profile by id
<details> 
<summary> Typical GET response </summary>

	```
    {
      "id": 2,
      "user": "gooobles",
      "bio": "",
      "created_at": "12 Mar 2025",
      "image": "https://res.cloudinary.com/dt7dd37h8/image/upload/v1/media/../guitar-logo-white_utocxc",
      "is_user": false,
      "following_id": null,
      "following_count": 0,
      "followers_count": 0,
      "posts_count": 1
    }
	```

</details>

<br />

`PUT` : Update a profile by id

### /followers

`GET` : Get all followers

<details> 
<summary> Typical GET response </summary>

	```
    {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 3,
                "user": "gooobles",
                "followed": 1,
                "followed_name": "differi",
                "created_at": "18 Mar 2025"
            },
            {
                "id": 2,
                "user": "differi",
                "followed": 4,
                "followed_name": "gooobles",
                "created_at": "18 Mar 2025"
            },
            {
                "id": 1,
                "user": "differi",
                "followed": 2,
                "followed_name": "friz",
                "created_at": "16 Mar 2025"
            }
        ]
    }
	```
</details>

<br />

`POST` : Create a follower

### /followers/:id

`GET` : Get a follower by id
<details> 
<summary> Typical GET response </summary>

	```
    {
        "id": 3,
        "user": "gooobles",
        "followed": 1,
        "followed_name": "differi",
        "created_at": "18 Mar 2025"
    }
	```

</details>

<br />

`DELETE` : Delete a follower by id

### /posts

`GET` : Get all posts
<details> 
<summary> Typical GET response </summary>

	```
    {
      "count": 4,
      "next": null,
      "previous": null,
      "results": [
        {
          "id": 6,
          "user": "differi",
          "user_image": "https://res.cloudinary.com/dt7dd37h8/image/upload/v1/media/../guitar-logo-white_utocxc",
          "is_user": false,
          "title": "My biggest song!",
          "updated_at": "18 Mar 2025",
          "created_at": "18 Mar 2025",
          "content": "Here is a clip of my biggest song.",
          "song": 2,
          "net_votes": 0
        },
        {
          "id": 5,
          "user": "gooobles",
          "user_image": "https://res.cloudinary.com/dt7dd37h8/image/upload/v1/media/../guitar-logo-white_utocxc",
          "is_user": false,
          "title": "cornerhouse",
          "updated_at": "17 Mar 2025",
          "created_at": "17 Mar 2025",
          "content": "come to the cornerhouse on alternate tuesdays\r\n\r\npeace",
          "song": null,
          "net_votes": 0
        },
        {
          "id": 4,
          "user": "differi",
          "user_image": "https://res.cloudinary.com/dt7dd37h8/image/upload/v1/media/../guitar-logo-white_utocxc",
          "is_user": false,
          "title": "broadwater!!!",
          "updated_at": "17 Mar 2025",
          "created_at": "17 Mar 2025",
          "content": "please come to the broadwater at 7 on sunday!",
          "song": null,
          "net_votes": 0
        },
        {
          "id": 3,
          "user": "differi",
          "user_image": "https://res.cloudinary.com/dt7dd37h8/image/upload/v1/media/../guitar-logo-white_utocxc",
          "is_user": false,
          "title": "my post!",
          "updated_at": "17 Mar 2025",
          "created_at": "17 Mar 2025",
          "content": "hi this is my content. no song attached.",
          "song": null,
          "net_votes": 0
        }
      ]
    }
	```
</details>

<br />

`POST` : Create a post

### /posts/:id

`GET` : Get a post by id
<details> 
<summary> Typical GET response </summary>

	```
    {
      "id": 3,
      "user": "differi",
      "user_image": "https://res.cloudinary.com/dt7dd37h8/image/upload/v1/media/../guitar-logo-white_utocxc",
      "is_user": false,
      "title": "my post!",
      "updated_at": "17 Mar 2025",
      "created_at": "17 Mar 2025",
      "content": "hi this is my content. no song attached.",
      "song": 2,
      "net_votes": 0
    }
	```

</details>

<br />

`PUT` : Update a post by id

`DELETE` : Delete a post by id

### /comments

`GET` : Get all comments
<details> 
<summary> Typical GET response </summary>

	```
    {
      "count": 2,
      "next": null,
      "previous": null,
      "results": [
        {
          "id": 2,
          "user": "friz",
          "is_user": false,
          "created_at": "17 Mar 2025",
          "content": "another comment!",
          "post": 1
        },
        {
          "id": 1,
          "user": "differi",
          "is_user": true,
          "created_at": "17 Mar 2025",
          "content": "comment on a post!",
          "post": 1
        }
      ]
    }
	```

</details>

<br />

`POST` : Create a comment

### /comments/:id

`GET` : Get a comment by id

<details> 
<summary> Typical GET response </summary>

	```
    {
        "id": 2,
        "user": "friz",
        "is_user": false,
        "created_at": "17 Mar 2025",
        "content": "another comment!",
        "post": 1
    }
	```

</details>

<br />

`PUT` : Update a comment by id

`DELETE` : Delete a comment by id

### /post_votes

`GET` : Get all post votes
<details> 
<summary> Typical GET response </summary>

	```
    {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 3,
                "user": "gooobles",
                "is_user": false,
                "post": 1,
                "created_at": "17 Mar 2025",
                "downvote": true
            },
            {
                "id": 2,
                "user": "friz",
                "is_user": false,
                "post": 1,
                "created_at": "17 Mar 2025",
                "downvote": false
            },
            {
                "id": 1,
                "user": "differi",
                "is_user": true,
                "post": 1,
                "created_at": "17 Mar 2025",
                "downvote": false
            }
        ]
    }
	```

</details>

<br />

`POST` : Create a post vote

### /post_votes/:id

`GET` : Get a post vote by id

<details> 
<summary> Typical GET response </summary>

	```
    {
        "id": 3,
        "user": "gooobles",
        "is_user": false,
        "post": 1,
        "created_at": "17 Mar 2025",
        "downvote": true
    }
	```

</details>

<br />

`PUT` : Update a post vote by id

`DELETE` : Delete a post vote by id

### /songs

`GET` : Get all songs
<details> 
<summary> Typical GET response </summary>

	```
    {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 3,
                "user": "friz",
                "is_user": false,
                "title": "totally not wayward",
                "updated_at": "17 Mar 2025",
                "created_at": "17 Mar 2025",
                "audio_url": "http://res.cloudinary.com/dt7dd37h8/raw/upload/v1742247417/audio_files/fmjn45alkem7ducr3krj.wav",
                "net_votes": 0,
                "artist_name": "barry shcmeter schmiles",
                "link_to_song": ""
            },
            {
                "id": 2,
                "user": "differi",
                "is_user": true,
                "title": "wayward",
                "updated_at": "17 Mar 2025",
                "created_at": "17 Mar 2025",
                "audio_url": "http://res.cloudinary.com/dt7dd37h8/raw/upload/v1742246817/audio_files/evuqcl5oq8jmjzpwr9fn.wav",
                "net_votes": -1,
                "artist_name": "Harry Peter Miles",
                "link_to_song": ""
            }
        ]
    }
	```

</details>

<br />

`POST` : Create a song

### /songs/:id

`GET` : Get a song by id

<details> 
<summary> Typical GET response </summary>

	```
    {
        "id": 2,
        "user": "differi",
        "is_user": true,
        "title": "wayward",
        "updated_at": "17 Mar 2025",
        "created_at": "17 Mar 2025",
        "audio_url": "http://res.cloudinary.com/dt7dd37h8/raw/upload/v1742246817/audio_files/evuqcl5oq8jmjzpwr9fn.wav",
        "net_votes": -1,
        "artist_name": "Harry Peter Miles",
        "link_to_song": ""
    }
	```

</details>

<br />

`PUT` : Update a song

`DELETE` : Delete a song


### /song_votes

`GET` : Get all song votes
<details> 
<summary> Typical GET response </summary>

	```
    {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 3,
                "user": "gooobles",
                "is_user": false,
                "song": 2,
                "created_at": "17 Mar 2025",
                "downvote": false
            },
            {
                "id": 2,
                "user": "friz",
                "is_user": false,
                "song": 2,
                "created_at": "17 Mar 2025",
                "downvote": true
            },
            {
                "id": 1,
                "user": "differi",
                "is_user": true,
                "song": 2,
                "created_at": "17 Mar 2025",
                "downvote": true
            }
        ]
    }
	```

</details>

<br />

`POST` : Create a song vote

### /song_votes/:id

`GET` : Get a song vote by id

<details> 
<summary> Typical GET response </summary>

	```
    {
        "id": 2,
        "user": "friz",
        "is_user": false,
        "song": 2,
        "created_at": "17 Mar 2025",
        "downvote": true
    }
	```

</details>

<br />

`PUT` : Update a song vote by id

`DELETE` : Delete a song vote by id



### CREDITS

default user icon
https://www.flaticon.com/free-icon/guitar_5018387?related_id=5018352&origin=search
