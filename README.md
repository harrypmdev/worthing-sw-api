# Worthing SW API

This repository is the back-end REST API for the Worthing Sound Wave project.

Live Site - https://worthing-sw-c84ec9c15d42.herokuapp.com/

Live API -

Front-End Repository and READM.md - https://github.com/harrypmdev/worthing-sw

# Contents

- [**Objective**](#objective)
- [**Entity Relationship Diagram**](#)
- [**API Endpoints Overview**](#api-endpoints-overview)
  - [/profiles](#profiles)
  - [/profiles/:id](#profilesid)
  - [/followers](#followers)
  - [/followers/:id](#followersid)
  - [/posts](#posts)
  - [/posts/:id](#postsid)
  - [/comments](#comments)
  - [/comments/:id](#comments/:id)
  - [/post_votes](#post_votes)
  - [/post_votes/:id](#post_votesid)
  - [/songs](#songs)
  - [/songs/:id](#songsid)
  - [/songs_votes](#song_votesid)
  - [/songs_votes/:id](#song_votesid')
- [**Deployment**](#deployment)
- [**Validation**](#validation)
- [**Credits and References**](#credits--references)
  - [Code, Dependencies and Tools](#code-dependencies-and-tools)
  - [Media](#media)

# Objective

The objective of this REST API is to provide a secure and comprehensive means of providing data to the Worthing Sound Wave
website front-end. The CRUD functionality and filter functionality combined with solid authentication and validation security
provides the foundation for the React front-end to provide a high quality user experience.

# Entity Relationship Diagram

+ The entity relationship diagram visualises the data schema used in this back-end.
+ Depicted on the diagram, abstract classes are utilised as allowed in Django's REST framework for better code reuse and simplification.
+ <code>SongVote</code> and <code>PostVote</code> share fields, and so both inherit from <code>Vote</code> (abstract) which has all the shared fields.
+ Similarly, <code>Post</code> and <code>Song</code> both share fields, so both inherit from <code>BaseContent</code> (abstract) which has the shared fields.
+ This design makes any future expansion of site features easy, as any model similar to <code>SongVote</code> or <code>PostVote</code> can inherit from
<code>Vote</code>, and likewise for <code>BaseContent</code>.

![ER Diagram](/readme-assets/ER-diagram.webp)

# API Endpoints Overview

The following is an overview of the HTTP requests available for the API endpoints, and typical
GET request responses.
Very detailed, comprehensive docstrings for all models, serializers and views are included in the repository code itself.

## /profiles

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

## /profiles/:id

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

## /followers

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

## /followers/:id

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

## /posts

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

## /posts/:id

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

## /comments

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

## /comments/:id

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

## /post_votes

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

## /post_votes/:id

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

## /songs

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

## /songs/:id

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


## /song_votes

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

## /song_votes/:id

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

# Validation

+ <a href="https://flake8.pycqa.org/en/latest/">Flake8</a> PEP8 enforcer was used throughout development, and flagged no warnings with the finished code.

![Flake8](/readme-assets/flake8.webp)

# Credits and References

## Code, Dependencies and Tools

+ Built using the <a href="https://www.django-rest-framework.org/">Django REST framework</a>.
+ <a href="https://flake8.pycqa.org/en/latest/#">Flake8</a> PEP8 enforcer used to ensure consistent PEP8 styling.

## Media

+ <a href="https://www.flaticon.com/free-icon/guitar_5018387?related_id=5018352&origin=search">Default User Icon</a> for new profiles <a href="https://www.flaticon.com/free-icons/music-and-multimedia" title="music and multimedia icons"> created by Good Ware - Flaticon</a>


