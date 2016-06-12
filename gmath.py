def calculate_normal( ax, ay, az, bx, by, bz ):
    normal = [0,0,0]
    normal[0] = ay * bz - az * by
    normal[1] = az * bx - ax * bz
    normal[2] = ax * by - ay * bx
    return normal

def light_normal( points, i ):
    #get as and bs to calculate the normal
    ax = points[i + 1][0] - points[ i ][0]
    ay = points[i + 1][1] - points[ i ][1]
    az = points[i + 1][2] - points[ i ][2]

    bx = points[i + 2][0] - points[ i ][0]
    by = points[i + 2][1] - points[ i ][1]
    bz = points[i + 2][2] - points[ i ][2]

    normal = calculate_normal( ax, ay, az, bx, by, bz )

    return normal

def normal(vector):
    magnitude = sqrt(vector[0] * vector[0] + vector[1] * vector[1] + vector[2] * vector[2])
    if magnitude == 0:
        return 0
    return [vector[x] / magnitude for x in range(3)]

def dot_product(vector0, vector1):
    return vector0[0] * vector1[0] + vector0[1] * vector1[1] + vector0[2] * vector1[2]

def scalar_product(vector, scalar):
    return [vector[x] * scalar for x in range(len(vector))]

def vector_subtract(vector0, vector1):
    return [vector0[x] - vector1[x] for x in range(len(vector0))]

def calculate_dot( points, i ):
    #get as and bs to calculate the normal
    ax = points[i + 1][0] - points[ i ][0]
    ay = points[i + 1][1] - points[ i ][1]
    az = points[i + 1][2] - points[ i ][2]

    bx = points[i + 2][0] - points[ i ][0]
    by = points[i + 2][1] - points[ i ][1]
    bz = points[i + 2][2] - points[ i ][2]

    normal = calculate_normal( ax, ay, az, bx, by, bz )

    #set up the view vector values
    vx = 0
    vy = 0
    vz = -1

    #calculate the dot product
    dot = normal[0] * vx + normal[1] * vy + normal[2] * vz

    return dot
