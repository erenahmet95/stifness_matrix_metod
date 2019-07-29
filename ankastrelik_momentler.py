def  single_load(load,a,b,ari = 4,brj=2):
    L = a+b
    delta_i = load*b*(L**2-b**2)/(6*L)

    delta_j = load*a*(L**2-a**2)/(6*L)

    ankastre_moment_i =(ari*delta_i-brj*delta_j)/L
    ankastre_moment_j =(brj*delta_i-ari*delta_j)/L


    start_point_load =(ankastre_moment_i+ankastre_moment_j+load*b)/L

    end_point_load = load-start_point_load

    result = [0,start_point_load,ankastre_moment_i,0,end_point_load,ankastre_moment_j]

    return result

## İki ucu mafsallı cubuklarda ari,brj değerleri 0 oluurr ??????????????


def distrubuted_load(load,a,b,c,ari = 4,brj=2) :

    L = a+b

    delta_i = load*b*c*((4*a(b+L)-c**2))/(24*L)
    delta_j = load*a*c*((4*b(a+L)-c**2))/(24*L)

    ankastre_moment_i = (ari*delta_i-brj*delta_j)/L
    ankastre_moment_j = (brj*delta_i-ari*delta_j)/L

    start_point_load = (ankastre_moment_i+ankastre_moment_j+load*c*b)/L
    end_point_load = load*c-start_point_load

    result = [0,start_point_load,ankastre_moment_i,0,end_point_load,ankastre_moment_j]


    return result

def single_moment(moment,a,b,ari = 4,brj=2):

    L = a+b

    delta_i = -1*moment*(3*b**2-L**2)/(6*L)
    delta_j = -1*(moment)*(L**2-3*a**2)/(L*6)

    ankastre_moment_i = (ari*delta_i-brj*delta_j)/L
    ankastre_moment_j = (brj*delta_i-ari*delta_j)/L

    start_point_load = (ankastre_moment_i+ankastre_moment_j+moment)/L
    end_point_load = -1 * start_point_load

    result = [0,start_point_load,ankastre_moment_i,0,end_point_load,ankastre_moment_j]

    return result


def trapez_load1(load,a,b,c,ari = 4,brj=2):

    L = a+b

    alfa = a/L
    beta = b/L
    gama = c/L

    delta_i = load*L**3*alfa*(270*(alfa-alfa**3)-alfa**2*(45*alfa-2*alfa))/3240

    delta_j = load*L**3*alfa*(270*(beta-beta**3)-alfa**2*(45*beta+2*alfa))/3240

    ankastre_moment_i = (ari*delta_i-brj*delta_j)/L
    ankastre_moment_j = (brj*delta_i-ari*delta_j)/L

    start_point_load = (ankastre_moment_i+ankastre_moment_j+0.5*load*c*b)/L

    end_point_load = 0.5*load*c-start_point_load

    result = [0,start_point_load,ankastre_moment_i,0,end_point_load,ankastre_moment_j]

    return result

def trapez_load2(load,a,b,c,ari = 4,brj=2):

    L = a+b

    alfa = a/L
    beta = b/L
    gama = c/L

    delta_i = load*L**3*alfa*(270*(alfa-alfa**3)-alfa**2*(45*alfa+2*alfa))/3240

    delta_j = load*L**3*alfa*(270*(beta-beta**3)-alfa**2*(45*beta-2*alfa))/3240

    ankastre_moment_i = (ari*delta_i-brj*delta_j)/L

    ankastre_moment_j = (brj*delta_i-ari*delta_j)/L

    start_point_load = (ankastre_moment_i+ankastre_moment_j+0.5*load*c*b)/L

    end_point_load = 0.5*load*c-start_point_load

    result = [0,start_point_load,ankastre_moment_i,0,end_point_load,ankastre_moment_j]

    return result
