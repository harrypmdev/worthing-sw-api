# Worthing SW API

This repository is the back-end REST API for the Worthing Sound Wave project.

Live Site - https://worthing-sw-c84ec9c15d42.herokuapp.com/

Live API - https://worthing-sw-api-fc5a7cd44915.herokuapp.com/

Front-End Repository and README.md - https://github.com/harrypmdev/worthing-sw

# Contents

- [**Objective**](#objective)
- [**Technologies Used**](#technologies-used)
- [**Entity Relationship Diagram**](#entity-relationship-diagram)
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
  - [/songs_votes](#song_votes)
  - [/songs_votes/:id](#song_votesid)
  - [/venues/](#venues)
  - [/user_venues/](#user_venues)
  - [/user_venues/:id](#user_venuesid)
- [**Validation**](#validation)
- [**Deployment**](#deployment)
- [**Credits and References**](#credits--references)
  - [Code, Dependencies and Tools](#code-dependencies-and-tools)
  - [Media](#media)

# Objective

The objective of this REST API is to provide a secure and comprehensive means of providing data to the Worthing Sound Wave
website front-end. The CRUD functionality and filter functionality combined with solid authentication and validation security
provides the foundation for the React front-end to provide a high quality user experience.

# Technologies Used

## Languages

+ Python - The primary language of the entire back-end.

## Libraries and Frameworks

+ <a href='https://www.djangoproject.com/'>Django</a> and its REST framework - A backend framework for creating RESTful APIs
+ <a href='https://cloudinary.com/'>Cloudinary</a> python libraries and cloudinary service - for image and audio uploads from Django and then online hosting

# Entity Relationship Diagram

+ The entity relationship diagram visualises the data schema used in this back-end.

+ Depicted on the diagram, abstract classes are utilised as allowed in Django's REST framework for better code reuse and simplification.
+ <code>SongVote</code> and <code>PostVote</code> share fields, and so both inherit from <code>Vote</code> (abstract) which has all the shared fields.
+ Similarly, <code>Post</code> and <code>Song</code> both share fields, so both inherit from <code>BaseContent</code> (abstract) which has the shared fields.
+ This design makes any future expansion of site features easy, as any model similar to <code>SongVote</code> or <code>PostVote</code> can inherit from
<code>Vote</code>, and likewise for <code>BaseContent</code>.

+ Also depicted on the diagram is a many-to-many relationship between User and Venue. Though Django has built in many-to-many functionality, a custom
junction table was deemed the best implementation for the needs of the feature.

![ER Diagram](/readme-assets/ER-diagram.webp)

# API Endpoints Overview

The following is an overview of the HTTP requests available for the API endpoints, and typical
GET request responses.
Very detailed, comprehensive docstrings for all models, serializers and views are included in the repository code itself.

## /profiles

`GET` : Get profiles in list view
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

`GET` : Get followers in list view

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

`GET` : Get posts in list view
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

`GET` : Get comments in list view
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

`GET` : Get post votes in list view
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

`GET` : Get songs in list view
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

`GET` : Get song votes in list view
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

## /venues/

`GET` : Get venues in list view

<details> 
<summary> Typical GET response </summary>

	```
    {
      "count": 10,
      "next": null,
      "previous": null,
      "results": [
        {
          "id": 1,
          "name": "The Broadwater",
          "user_count": 1
        },
        {
          "id": 2,
          "name": "The Cornerhouse",
          "user_count": 1
        },
        {
          "id": 3,
          "name": "The Cricketers",
          "user_count": 0
        },
        {
          "id": 4,
          "name": "The Mulberry",
          "user_count": 2
        },
        {
          "id": 5,
          "name": "The New Amsterdam",
          "user_count": 2
        },
        {
          "id": 6,
          "name": "O'Connor's on Warwick Street",
          "user_count": 0
        },
        {
          "id": 7,
          "name": "The Thieves Kitchen",
          "user_count": 0
        },
        {
          "id": 8,
          "name": "The Brewhouse",
          "user_count": 0
        },
        {
          "id": 9,
          "name": "The Park View",
          "user_count": 0
        },
        {
          "id": 10,
          "name": "Slug and Lettuce Bar",
          "user_count": 0
        }
      ]
    }
	```

</details>

<br />

## /user_venues/

`GET` : Get user venues in list view

<details> 
<summary> Typical GET response </summary>

	```
    {
      "count": 6,
      "next": null,
      "previous": null,
      "results": [
        {
          "id": 32,
          "user": 3,
          "venue": 5,
          "user_name": "bibble",
          "name": "The New Amsterdam",
          "user_count": 2,
          "created_at": "04 Apr 2025"
        },
        {
          "id": 31,
          "user": 3,
          "venue": 2,
          "user_name": "bibble",
          "name": "The Cornerhouse",
          "user_count": 1,
          "created_at": "04 Apr 2025"
        },
        {
          "id": 29,
          "user": 3,
          "venue": 4,
          "user_name": "bibble",
          "name": "The Mulberry",
          "user_count": 2,
          "created_at": "04 Apr 2025"
        },
        {
          "id": 27,
          "user": 1,
          "venue": 4,
          "user_name": "differi",
          "name": "The Mulberry",
          "user_count": 2,
          "created_at": "04 Apr 2025"
        },
        {
          "id": 24,
          "user": 1,
          "venue": 1,
          "user_name": "differi",
          "name": "The Broadwater",
          "user_count": 1,
          "created_at": "04 Apr 2025"
        },
        {
          "id": 22,
          "user": 1,
          "venue": 5,
          "user_name": "differi",
          "name": "The New Amsterdam",
          "user_count": 2,
          "created_at": "04 Apr 2025"
        }
      ]
    }
	```

</details>

<br />

`POST` : Add a UserVenue

## /user_venues/:id

`GET` : Get user venue by id

<details> 
<summary> Typical GET response </summary>

	```
    {
      "id": 27,
      "user": 1,
      "venue": 4,
      "user_name": "differi",
      "name": "The Mulberry",
      "user_count": 2,
      "created_at": "04 Apr 2025"
    }
	```

</details>

<br />

`DELETE` : Delete a user venue

# Testing

## Automated Testing

The testing for this site was primarily done manually.
Some automated testing was done however to check the correct functioning of the venues user_count method field.
This testing can be found in <code>venues/tests.py</code>.

## Manual Testing

The API has been thoroughly tested using:
  + The browser
  + Powershell Invoke-WebRequest commands
  + JS axios requests in the front-end

A write-up of manual tests follows:

|  App | Endpoint |Testing action | Response Status Code | Outcome |
|---|---|---|---|---|
profiles|<code>/profiles</code>|GET request| 200 (OK) | Receive a list of all profiles including useful serializer fields|
profiles|<code>/profiles/:id</code>|GET request for an existing profile| 200 (OK) |Receive the profile information|
profiles|<code>/profiles/:id</code>|GET request for a non-existing profile| 404 (Not Found) |A detail JSON returns with the content 'No Profile matches the given query'|
profiles|<code>/profiles/:id</code>|PUT request but not authenticated| 401 (Unauthorised) | A detail JSON returns with the content 'Authentication credentials were not provided'|
followers|<code>/followers</code>|GET request| 200 (OK) | Receive a list of all followers|
followers|<code>/followers</code>|POST request but not authenticated| 401 (Unauthorised) | A detail JSON returns with the content 'Authentication credentials were not provided'
followers|<code>/followers</code>|POST request and authenticated| 201 (Created) | The new Follower is returned
followers|<code>/followers/:id</code>|DELETE request and unauthenticated| 401 (Unauthorised)| A detail JSON returns with the content 'Authentication credentials were not provided'
followers|<code>/followers/:id</code>|DELETE request and authenticated| 204 (No Content)| No response content as status code indicates successful deletion
posts|<code>/posts</code>|GET request with ordering by -net_votes| 200 (OK) | Receive the post information with highest net votes first
posts|<code>/posts</code>|GET request with search query a username| 200 (OK) | Receive the post information, filtered to include only posts by the username searched or posts with this username in the title
posts|<code>/posts</code>|POST request and authenticated| 201 (OK) | Receive the post information for the post that has just been created, including information that will be new to me as the client such as an id
posts|<code>/posts/:id</code>|PUT request and authenticated| 200 (OK) | Receive the updated information for the post in question
posts|<code>/posts/:id</code>|DELETE request and authenticated| 204 (No Content) | No response content as status code indicates successful deletion
comments|<code>/comments</code>|GET request filtering by a particular user| 200 (OK) | Receive comments only from the user in question
comments|<code>/comments</code>|GET request filtering by a particular post| 200 (OK) | Receive the comments made on the post in question only
comments|<code>/comments/:id</code>|GET request| 200 (OK) | Receive the data of a specific content
comments|<code>/comments/:id</code>|PUT request and authenticated but with a content 500 characters long| 400 (Bad Request) | A JSON returns an error for 'content' with the content 'Ensure this field has no more than 300 characters'|
post_votes|<code>/post_votes</code>|GET request | 200 (OK) | Receive a list of all post votes|
post_votes|<code>/post_votes/:id</code>|PUT request and authenticated to change downvote field| 200 (OK) | Receive back data with changed downvote field|
post_votes|<code>/post_votes/:id</code>|DELETE request | 204 (No Content) | No response content as status code indicates successful deletion|
song_votes|<code>/song_votes</code>|GET request | 200 (OK) | Receive a list of all song votes|
song_votes|<code>/song_votes</code>|GET request filtering by a particular user| 200 (OK) | Receive a list of song votes, only those belonging to the given user|
song_votes|<code>/song_votes/:id</code>|GET request for an id that doesn't exist| 404 (Not Found)| Receive a detail JSON with the content 'No SongVote matches the given query'|
song_votes|<code>/song_votes/:id</code>|DELETE request when authorised, but not as the user the song vote belongs to| 403 (Forbidden)| A detail JSON returns with the content 'you do not have permission to perform this action'.|
songs|<code>/songs</code>|GET request with the user__followed__user filter| 200 (OK) | Receive a list of songs, but only songs from users the given user is following
songs|<code>/songs</code>|GET request with a user__followed__filter and an invalid user| 400 (Bad Request) | Receive a JSON response with a "user__followed__user" field with the content "Select a valid choice. That choice is not one of the available choices."|
songs|<code>/songs/:id</code>|GET request with a valid id| 200 (OK) | Receive the data for the specific id request|
songs|<code>/songs/:id</code>|GET request and unauthorised| 200 (OK) | Receive data as normal, as read-only requests do not require authorisation|
venues|<code>/venues</code>|POST request and authorised| 405 (Method Not Allowed) | Receive a detail JSON informing the POST request is not allowed. This is because POST requests are not allowed, the venues are preset
venues|<code>/venues</code>|GET request and unauthorised| 200 (OK) | Receive the venue data as normal as is read only|
user_venues|<code>/user_venues</code>|GET request with filter to a particular venue| 200 (OK) | Receive UserVenue data for only the venue provided|
user_venues|<code>/user_venues</code>|GET request with filter to a particular user| 200 (OK) | Receive UserVenue data for only the user provided|
user_venues|<code>/user_venues/:id</code>|DELETE request and authorised| 204 (No Content) | No response content as status code indicates successful deletion

<br />

# Validation

# Deployment

+ <a href="https://flake8.pycqa.org/en/latest/">Flake8</a> PEP8 enforcer was used throughout development, and flagged no warnings with the finished code.

![Flake8](/readme-assets/flake8.webp)

# Credits and References

## Code, Dependencies and Tools

+ Built using the <a href="https://www.django-rest-framework.org/">Django REST framework</a>.
+ <a href="https://flake8.pycqa.org/en/latest/#">Flake8</a> PEP8 enforcer used to ensure consistent PEP8 styling.
+ ER diagram created with <a href="https://www.lucidchart.com/pages">Lucidchart</a>.

## Media

+ <a href="https://www.flaticon.com/free-icon/guitar_5018387?related_id=5018352&origin=search">Default User Icon</a> for new profiles <a href="https://www.flaticon.com/free-icons/music-and-multimedia" title="music and multimedia icons"> created by Good Ware - Flaticon</a>


