create table users(
	id serial primary key,
	username character varying(50) unique,
	"password" character varying(140)
);


create table tokens(
    id serial primary key,
	user_id int  references users(id),
	"token" character varying(140)
)