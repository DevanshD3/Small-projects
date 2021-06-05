SELECT a.*,b.starnum
from
    (
        SELECT projects.id as id, projects.name,description,
        array_agg(tags.name) as tag_names,view from projects
        LEFT JOIN taggings ON taggings.project_id = projects.id
        LEFT JOIN tags ON tags.id = taggings.tag_id
        where projects.project_access_type = 'Public' and
        projects.forked_project_id is NULL
        GROUP BY projects.id
    ) as a,
    (
        select project_id,count(id) as starnum from stars group by project_id
    ) as b
where a.id = b.project_id;