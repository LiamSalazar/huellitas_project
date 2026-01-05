-- ======================================================
-- HUELLITAS BD
-- ======================================================

-- ======================================================
-- CATÁLOGOS BASE
-- ======================================================

CREATE TABLE "Direccion" (
  id_Direccion SERIAL PRIMARY KEY,
  estado_Direccion              VARCHAR(80)  NOT NULL,
  municipio_Direccion           VARCHAR(120) NOT NULL,
  colonia_Direccion             VARCHAR(120),
  calle_Direccion               VARCHAR(120),
  numero_exterior_Direccion     VARCHAR(30),
  numero_interior_Direccion     VARCHAR(30),
  codigo_postal_Direccion       VARCHAR(10)
);

-- ======================================================
-- CATÁLOGOS ANIMALES
-- ======================================================

CREATE TABLE "AnimalEspecie" (
  id_AnimalEspecie SERIAL PRIMARY KEY,
  nombre_AnimalEspecie VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE "AnimalSexo" (
  id_AnimalSexo SERIAL PRIMARY KEY,
  nombre_AnimalSexo VARCHAR(12) NOT NULL UNIQUE
);

CREATE TABLE "AnimalTalla" (
  id_AnimalTalla SERIAL PRIMARY KEY,
  nombre_Talla VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE "AnimalTipo" (
  id_AnimalTipo SERIAL PRIMARY KEY,
  nombre_AnimalTipo VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE "AnimalFuncion" (
  id_AnimalFuncion SERIAL PRIMARY KEY,
  nombre_AnimalFuncion VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE "MedioLlegada" (
  id_MedioLlegada SERIAL PRIMARY KEY,
  nombre_MedioLlegada VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE "PatronPelaje" (
  id_PatronPelaje SERIAL PRIMARY KEY,
  nombre_PatronPelaje VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE "ColorOjos" (
  id_ColorOjos SERIAL PRIMARY KEY,
  nombre_ColorOjos VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE "ColorPrincipal" (
  id_ColorPrincipal SERIAL PRIMARY KEY,
  nombre_ColorPrincipal VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE "RazaPerro" (
  id_RazaPerro SERIAL PRIMARY KEY,
  nombre_RazaPerro VARCHAR(120) NOT NULL UNIQUE
);

CREATE TABLE "RazaGato" (
  id_RazaGato SERIAL PRIMARY KEY,
  nombre_RazaGato VARCHAR(120) NOT NULL UNIQUE
);

CREATE TABLE "IdentificadorTipo" (
  id_IdentificadorTipo SERIAL PRIMARY KEY,
  nombre_IdentificadorTipo VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE "AnimalCaracter" (
  id_AnimalCaracter SERIAL PRIMARY KEY,
  nombre_AnimalCaracter VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE "AnimalEstado" (
  id_AnimalEstado SERIAL PRIMARY KEY,
  nombre_AnimalEstado VARCHAR(40) NOT NULL UNIQUE
);

-- ======================================================
-- CATÁLOGOS PERSONAS / PROCESOS / EVENTOS
-- ======================================================

CREATE TABLE "ViviendaTipo" (
  id_ViviendaTipo SERIAL PRIMARY KEY,
  nombre_ViviendaTipo VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE "PersonaSexo" (
  id_PersonaSexo SERIAL PRIMARY KEY,
  nombre_PersonaSexo VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE "VoluntarioRol" (
  id_VoluntarioRol SERIAL PRIMARY KEY,
  nombre_VoluntarioRol VARCHAR(40) NOT NULL UNIQUE
);

CREATE TABLE "ProcesoAdopcionEstado" (
  id_ProcesoAdopcionEstado SERIAL PRIMARY KEY,
  nombre_ProcesoAdopcionEstado VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE "AdoptanteNivelEconomico" (
  id_AdoptanteNivelEconomico SERIAL PRIMARY KEY,
  nombre_AdoptanteNivelEconomico VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE "BlacklistMotivo" (
  id_BlacklistMotivo SERIAL PRIMARY KEY,
  nombre_BlacklistMotivo VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE "EventoTipo" (
  id_EventoTipo SERIAL PRIMARY KEY,
  nombre_EventoTipo VARCHAR(40) NOT NULL UNIQUE
);

-- ======================================================
-- CATÁLOGOS MÉDICOS
-- ======================================================

CREATE TABLE "VacunaCatalogo" (
  id_VacunaCatalogo SERIAL PRIMARY KEY,
  nombre_VacunaCatalogo VARCHAR(120) NOT NULL UNIQUE,
  dias_vigencia_VacunaCatalogo INT NOT NULL CHECK (dias_vigencia_VacunaCatalogo > 0),
  dias_refuerzo_VacunaCatalogo INT CHECK (dias_refuerzo_VacunaCatalogo > 0) -- NULL = sin refuerzo
);

CREATE TABLE "AlergiaCatalogo" (
  id_AlergiaCatalogo SERIAL PRIMARY KEY,
  nombre_AlergiaCatalogo VARCHAR(120) NOT NULL UNIQUE
);

CREATE TABLE "PadecimientoCatalogo" (
  id_PadecimientoCatalogo SERIAL PRIMARY KEY,
  nombre_PadecimientoCatalogo VARCHAR(120) NOT NULL UNIQUE
);

CREATE TABLE "AntecedenteCatalogo" (
  id_AntecedenteCatalogo SERIAL PRIMARY KEY,
  nombre_AntecedenteCatalogo VARCHAR(120) NOT NULL UNIQUE
);

-- ======================================================
-- ENTIDADES (PERSONA, SEDE, VOLUNTARIO, ADOPTANTE)
-- ======================================================

CREATE TABLE "Persona" (
  id_Persona SERIAL PRIMARY KEY,
  nombre_Persona     VARCHAR(120) NOT NULL,
  apellidos_Persona  VARCHAR(120) NOT NULL,
  telefono_Persona   VARCHAR(20)  NOT NULL,
  email_Persona      VARCHAR(120) NOT NULL UNIQUE,
  pass_Persona       VARCHAR(255) NOT NULL,
  id_Direccion       INT REFERENCES "Direccion"(id_Direccion) ON DELETE SET NULL
);

CREATE TABLE "Sede" (
  id_Sede SERIAL PRIMARY KEY,
  nombre_Sede VARCHAR(120) NOT NULL UNIQUE,
  id_Direccion INT NOT NULL REFERENCES "Direccion"(id_Direccion) ON DELETE RESTRICT
);

CREATE TABLE "Voluntario" (
  id_Voluntario SERIAL PRIMARY KEY,
  id_Persona INT NOT NULL UNIQUE REFERENCES "Persona"(id_Persona) ON DELETE CASCADE,
  id_VoluntarioRol INT NOT NULL REFERENCES "VoluntarioRol"(id_VoluntarioRol),
  cedula_profesional_Voluntario VARCHAR(30), -- NULL = no tiene
  ruta_ine_Voluntario VARCHAR(300) NOT NULL,
  ruta_carta_compromiso_Voluntario VARCHAR(300) NOT NULL
);

-- Asignación histórica voluntario-sede
CREATE TABLE "VoluntarioSedeAsignacion" (
  id_Voluntario INT NOT NULL REFERENCES "Voluntario"(id_Voluntario) ON DELETE CASCADE,
  id_Sede INT NOT NULL REFERENCES "Sede"(id_Sede) ON DELETE RESTRICT,
  fecha_inicio TIMESTAMPTZ NOT NULL DEFAULT now(),
  fecha_fin    TIMESTAMPTZ,
  PRIMARY KEY (id_Voluntario, id_Sede, fecha_inicio),
  CHECK (fecha_fin IS NULL OR fecha_fin >= fecha_inicio)
);

-- Asistencia voluntarios
CREATE TABLE "VoluntarioAsistencia" (
  id_Voluntario INT NOT NULL REFERENCES "Voluntario"(id_Voluntario) ON DELETE CASCADE,
  id_Sede INT NOT NULL REFERENCES "Sede"(id_Sede) ON DELETE RESTRICT,
  entrada TIMESTAMPTZ NOT NULL,
  salida  TIMESTAMPTZ,
  PRIMARY KEY (id_Voluntario, id_Sede, entrada),
  CHECK (salida IS NULL OR salida >= entrada)
);

CREATE TABLE "Adoptante" (
  id_Adoptante SERIAL PRIMARY KEY,
  id_Persona INT NOT NULL UNIQUE REFERENCES "Persona"(id_Persona) ON DELETE CASCADE,

  id_ViviendaTipo INT NOT NULL REFERENCES "ViviendaTipo"(id_ViviendaTipo),
  metros_vivienda_Adoptante SMALLINT NOT NULL CHECK (metros_vivienda_Adoptante > 0),
  patio_Adoptante BOOLEAN NOT NULL,

  tiene_perros_Adoptante BOOLEAN NOT NULL,
  tiene_gatos_Adoptante BOOLEAN NOT NULL,

  ocupacion_Adoptante VARCHAR(120),
  edad_Adoptante SMALLINT NOT NULL CHECK (edad_Adoptante >= 18),

  id_PersonaSexo INT NOT NULL REFERENCES "PersonaSexo"(id_PersonaSexo),
  hijos_pequenos_Adoptante BOOLEAN NOT NULL,

  id_AdoptanteNivelEconomico INT NOT NULL REFERENCES "AdoptanteNivelEconomico"(id_AdoptanteNivelEconomico),

  ruta_identificacion_Adoptante VARCHAR(300),
  ruta_comprobante_domicilio_Adoptante VARCHAR(300),
  ruta_responsiva_Adoptante VARCHAR(300)
);

-- Blacklist (histórico)
CREATE TABLE "PersonaBlacklist" (
  id_PersonaBlacklist SERIAL PRIMARY KEY,
  id_Persona INT NOT NULL REFERENCES "Persona"(id_Persona) ON DELETE RESTRICT,
  id_BlacklistMotivo INT NOT NULL REFERENCES "BlacklistMotivo"(id_BlacklistMotivo),
  fecha_incidente TIMESTAMPTZ NOT NULL DEFAULT now(),
  detalle_incidente TEXT
);

-- ======================================================
-- FINANZAS (ACREEDORES Y CUENTAS POR PAGAR)
-- ======================================================

CREATE TABLE "Acreedor" (
  id_Acreedor SERIAL PRIMARY KEY,
  id_Persona INT REFERENCES "Persona"(id_Persona) ON DELETE SET NULL,
  nombre_Comercial_Acreedor VARCHAR(150) NOT NULL,
  rfc_Acreedor VARCHAR(15) UNIQUE
);

CREATE TABLE "CuentaPorPagar" (
  id_Cuenta SERIAL PRIMARY KEY,
  id_Acreedor INT NOT NULL REFERENCES "Acreedor"(id_Acreedor) ON DELETE RESTRICT,
  monto_Original NUMERIC(10,2) NOT NULL CHECK (monto_Original > 0),
  monto_Abonado  NUMERIC(10,2) NOT NULL DEFAULT 0 CHECK (monto_Abonado >= 0 AND monto_Abonado <= monto_Original),
  saldo_Pendiente NUMERIC(10,2) GENERATED ALWAYS AS (monto_Original - monto_Abonado) STORED,
  concepto_Deuda TEXT NOT NULL,
  fecha_Vencimiento DATE,
  estado_Pago VARCHAR(20) NOT NULL DEFAULT 'Pendiente'
);

-- ======================================================
-- RESCATE (REPORTE) + ANIMALES
-- ======================================================

CREATE TABLE "ReporteAnimal" (
  id_ReporteAnimal SERIAL PRIMARY KEY,
  id_Direccion INT NOT NULL REFERENCES "Direccion"(id_Direccion) ON DELETE RESTRICT,

  id_ColorPrincipal INT REFERENCES "ColorPrincipal"(id_ColorPrincipal),
  id_ColorOjos INT REFERENCES "ColorOjos"(id_ColorOjos),

  telefono_Reportante VARCHAR(20),
  ruta_foto_ReporteAnimal VARCHAR(300),

  fecha_ReporteAnimal TIMESTAMPTZ NOT NULL DEFAULT now(),
  id_VoluntarioAsignado INT REFERENCES "Voluntario"(id_Voluntario) ON DELETE SET NULL,
  id_SedeDestino INT REFERENCES "Sede"(id_Sede) ON DELETE SET NULL
);

CREATE TABLE "ReporteColorCombinacion" (
  id_ReporteAnimal INT NOT NULL REFERENCES "ReporteAnimal"(id_ReporteAnimal) ON DELETE CASCADE,
  id_ColorPrincipal INT NOT NULL REFERENCES "ColorPrincipal"(id_ColorPrincipal),
  PRIMARY KEY (id_ReporteAnimal, id_ColorPrincipal)
);

CREATE TABLE "Animal" (
  id_Animal SERIAL PRIMARY KEY,
  nombre_Animal VARCHAR(120) NOT NULL,
  clave_ruac_Animal VARCHAR(50) UNIQUE,

  id_AnimalEspecie INT NOT NULL REFERENCES "AnimalEspecie"(id_AnimalEspecie),
  id_AnimalSexo INT NOT NULL REFERENCES "AnimalSexo"(id_AnimalSexo),
  id_AnimalTalla INT NOT NULL REFERENCES "AnimalTalla"(id_AnimalTalla),
  id_AnimalTipo INT NOT NULL REFERENCES "AnimalTipo"(id_AnimalTipo),
  id_AnimalFuncion INT NOT NULL REFERENCES "AnimalFuncion"(id_AnimalFuncion),
  id_MedioLlegada INT NOT NULL REFERENCES "MedioLlegada"(id_MedioLlegada),
  id_PatronPelaje INT NOT NULL REFERENCES "PatronPelaje"(id_PatronPelaje),

  id_ColorOjos INT NOT NULL REFERENCES "ColorOjos"(id_ColorOjos),
  id_ColorPrincipal INT NOT NULL REFERENCES "ColorPrincipal"(id_ColorPrincipal),

  id_RazaPerro INT REFERENCES "RazaPerro"(id_RazaPerro),
  id_RazaGato  INT REFERENCES "RazaGato"(id_RazaGato),

  id_AnimalCaracter INT NOT NULL REFERENCES "AnimalCaracter"(id_AnimalCaracter),
  id_AnimalEstado INT NOT NULL REFERENCES "AnimalEstado"(id_AnimalEstado),

  peso_Animal NUMERIC(5,2) NOT NULL CHECK (peso_Animal > 0),

  edad_anios_Animal SMALLINT NOT NULL CHECK (edad_anios_Animal >= 0),
  edad_meses_Animal SMALLINT NOT NULL CHECK (edad_meses_Animal BETWEEN 0 AND 11),

  foto_perfil_Animal VARCHAR(300),

  fecha_registro_Animal TIMESTAMPTZ NOT NULL DEFAULT now(),
  id_Sede INT REFERENCES "Sede"(id_Sede) ON DELETE RESTRICT,

  id_ReporteAnimal INT REFERENCES "ReporteAnimal"(id_ReporteAnimal) ON DELETE SET NULL
);

CREATE INDEX idx_animal_fecha_registro ON "Animal"(fecha_registro_Animal);

CREATE TABLE "IdentificadorAnimal" (
  id_IdentificadorAnimal SERIAL PRIMARY KEY,
  id_Animal INT NOT NULL UNIQUE REFERENCES "Animal"(id_Animal) ON DELETE CASCADE,
  id_IdentificadorTipo INT NOT NULL REFERENCES "IdentificadorTipo"(id_IdentificadorTipo),
  valor_IdentificadorAnimal VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE "SaludAnimal" (
  id_SaludAnimal SERIAL PRIMARY KEY,
  id_Animal INT NOT NULL UNIQUE REFERENCES "Animal"(id_Animal) ON DELETE CASCADE,
  fecha_esterilizacion DATE
);

CREATE TABLE "AnimalVacuna" (
  id_Animal INT NOT NULL REFERENCES "Animal"(id_Animal) ON DELETE CASCADE,
  id_VacunaCatalogo INT NOT NULL REFERENCES "VacunaCatalogo"(id_VacunaCatalogo),
  fecha_aplicacion DATE NOT NULL,
  fecha_refuerzo DATE,
  PRIMARY KEY (id_Animal, id_VacunaCatalogo, fecha_aplicacion),
  CHECK (fecha_refuerzo IS NULL OR fecha_refuerzo >= fecha_aplicacion)
);

CREATE TABLE "AnimalAlergia" (
  id_Animal INT NOT NULL REFERENCES "Animal"(id_Animal) ON DELETE CASCADE,
  id_AlergiaCatalogo INT NOT NULL REFERENCES "AlergiaCatalogo"(id_AlergiaCatalogo),
  PRIMARY KEY (id_Animal, id_AlergiaCatalogo)
);

CREATE TABLE "AnimalPadecimiento" (
  id_Animal INT NOT NULL REFERENCES "Animal"(id_Animal) ON DELETE CASCADE,
  id_PadecimientoCatalogo INT NOT NULL REFERENCES "PadecimientoCatalogo"(id_PadecimientoCatalogo),
  PRIMARY KEY (id_Animal, id_PadecimientoCatalogo)
);

CREATE TABLE "AnimalAntecedente" (
  id_Animal INT NOT NULL REFERENCES "Animal"(id_Animal) ON DELETE CASCADE,
  id_AntecedenteCatalogo INT NOT NULL REFERENCES "AntecedenteCatalogo"(id_AntecedenteCatalogo),
  PRIMARY KEY (id_Animal, id_AntecedenteCatalogo)
);

-- colores adicionales (N:N)
CREATE TABLE "ColorCombinacion" (
  id_Animal INT NOT NULL REFERENCES "Animal"(id_Animal) ON DELETE CASCADE,
  id_ColorPrincipal INT NOT NULL REFERENCES "ColorPrincipal"(id_ColorPrincipal),
  PRIMARY KEY (id_Animal, id_ColorPrincipal)
);

-- fotos 1:N
CREATE TABLE "Fotografia" (
  id_Fotografia SERIAL PRIMARY KEY,
  id_Animal INT NOT NULL REFERENCES "Animal"(id_Animal) ON DELETE CASCADE,
  ruta_archivo_Fotografia VARCHAR(300) NOT NULL
);

-- Retiro de mascota
CREATE TABLE "RetiroMascota" (
  id_RetiroMascota SERIAL PRIMARY KEY,
  id_Persona INT NOT NULL REFERENCES "Persona"(id_Persona) ON DELETE RESTRICT,
  id_Animal INT NOT NULL REFERENCES "Animal"(id_Animal) ON DELETE RESTRICT,
  fecha_retiro TIMESTAMPTZ NOT NULL DEFAULT now(),
  id_BlacklistMotivo INT NOT NULL REFERENCES "BlacklistMotivo"(id_BlacklistMotivo)
);

-- ======================================================
-- ADOPCIONES (PROCESO + CITA ÚNICA POR PROCESO)
-- ======================================================

CREATE TABLE "ProcesoAdopcion" (
  id_ProcesoAdopcion SERIAL PRIMARY KEY,
  id_Animal INT NOT NULL REFERENCES "Animal"(id_Animal) ON DELETE RESTRICT,
  id_Adoptante INT NOT NULL REFERENCES "Adoptante"(id_Adoptante) ON DELETE RESTRICT,
  id_Voluntario INT REFERENCES "Voluntario"(id_Voluntario) ON DELETE SET NULL,
  id_ProcesoAdopcionEstado INT NOT NULL REFERENCES "ProcesoAdopcionEstado"(id_ProcesoAdopcionEstado),

  fecha_inicio_Proceso TIMESTAMPTZ NOT NULL DEFAULT now(),
  fecha_cierre_Proceso TIMESTAMPTZ,

  CHECK (fecha_cierre_Proceso IS NULL OR fecha_cierre_Proceso >= fecha_inicio_Proceso)
);

-- Regla: un animal puede tener historial, pero SOLO 1 proceso abierto a la vez
CREATE UNIQUE INDEX uq_proceso_adopcion_animal_abierto
ON "ProcesoAdopcion"(id_Animal)
WHERE fecha_cierre_Proceso IS NULL;

-- Cita 1:1 con el proceso (si se reprograma, UPDATE)
CREATE TABLE "ProcesoAdopcionCita" (
  id_ProcesoAdopcion INT PRIMARY KEY REFERENCES "ProcesoAdopcion"(id_ProcesoAdopcion) ON DELETE CASCADE,
  fecha_hora_cita TIMESTAMPTZ NOT NULL
);

-- ======================================================
-- DONACIONES
-- ======================================================

CREATE TABLE "Donacion" (
  id_Donacion SERIAL PRIMARY KEY,
  id_Persona INT REFERENCES "Persona"(id_Persona) ON DELETE SET NULL,
  monto_Donacion NUMERIC(10,2) NOT NULL CHECK (monto_Donacion > 0),
  fecha_Donacion TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ======================================================
-- EVENTOS
-- ======================================================

CREATE TABLE "Evento" (
  id_Evento SERIAL PRIMARY KEY,
  titulo_Evento VARCHAR(200) NOT NULL,
  descripcion_Evento TEXT NOT NULL,
  id_EventoTipo INT NOT NULL REFERENCES "EventoTipo"(id_EventoTipo),
  id_Sede INT NOT NULL REFERENCES "Sede"(id_Sede) ON DELETE RESTRICT,
  fecha_inicio_Evento TIMESTAMPTZ NOT NULL,
  fecha_fin_Evento TIMESTAMPTZ NOT NULL,
  cupo_maximo_Evento INT CHECK (cupo_maximo_Evento > 0),
  id_VoluntarioOrganizador INT REFERENCES "Voluntario"(id_Voluntario) ON DELETE SET NULL,
  CHECK (fecha_fin_Evento >= fecha_inicio_Evento)
);

CREATE TABLE "EventoAsistente" (
  id_Evento INT NOT NULL REFERENCES "Evento"(id_Evento) ON DELETE CASCADE,
  id_Persona INT NOT NULL REFERENCES "Persona"(id_Persona) ON DELETE CASCADE,
  PRIMARY KEY (id_Evento, id_Persona)
);

-- ======================================================
-- TRIGGERS (REGLAS DE NEGOCIO)
-- ======================================================

-- Función de sincronización
CREATE OR REPLACE FUNCTION trg_sync_animal_estado()
RETURNS trigger
LANGUAGE plpgsql
AS $$
DECLARE
  v_nombre_proceso_estado   TEXT;
  v_id_estado_disponible     INT;
  v_id_estado_en_proceso     INT;
  v_id_estado_adoptado       INT;
BEGIN
  -- Obtener el nombre del nuevo estado del proceso
  SELECT nombre_ProcesoAdopcionEstado INTO v_nombre_proceso_estado
  FROM "ProcesoAdopcionEstado" 
  WHERE id_ProcesoAdopcionEstado = NEW.id_ProcesoAdopcionEstado;

  -- SEGURIDAD: Seteo automático de fecha de cierre si el estado es final (Completado/Cancelado/Rechazado)
  IF v_nombre_proceso_estado IN ('Completado', 'Cancelado', 'Rechazado') THEN
      IF NEW.fecha_cierre_Proceso IS NULL THEN
          NEW.fecha_cierre_Proceso := now();
      END IF;
  ELSE
      -- Si el proceso se reabre o cambia a un estado no final, limpiamos la fecha de cierre
      NEW.fecha_cierre_Proceso := NULL;
  END IF;

  -- Cargar IDs de los estados del animal 
  SELECT id_AnimalEstado INTO v_id_estado_disponible FROM "AnimalEstado" WHERE nombre_AnimalEstado = 'Disponible';
  SELECT id_AnimalEstado INTO v_id_estado_en_proceso FROM "AnimalEstado" WHERE nombre_AnimalEstado = 'En proceso de adopcion';
  SELECT id_AnimalEstado INTO v_id_estado_adoptado FROM "AnimalEstado" WHERE nombre_AnimalEstado = 'Adoptado';

  -- Lógica de actualización en la tabla Animal
  IF v_nombre_proceso_estado IN ('Iniciado', 'Contactado', 'Cita programada', 'Convivencia aprobada', 'Documentacion en revision') THEN
    UPDATE "Animal" SET id_AnimalEstado = v_id_estado_en_proceso WHERE id_Animal = NEW.id_Animal;
    
  ELSIF v_nombre_proceso_estado = 'Completado' THEN
    UPDATE "Animal" SET id_AnimalEstado = v_id_estado_adoptado WHERE id_Animal = NEW.id_Animal;
    
  ELSIF v_nombre_proceso_estado IN ('Cancelado', 'Rechazado') THEN
    UPDATE "Animal" SET id_AnimalEstado = v_id_estado_disponible WHERE id_Animal = NEW.id_Animal;
  END IF;

  RETURN NEW;
END;
$$;

-- 2. Creación del Trigger (ÚNICO Y ESTRICTO)
-- Eliminamos cualquier rastro anterior para evitar el error de duplicidad
DROP TRIGGER IF EXISTS tg_sync_animal_estado ON "ProcesoAdopcion";

CREATE TRIGGER tg_sync_animal_estado
BEFORE INSERT OR UPDATE OF id_ProcesoAdopcionEstado ON "ProcesoAdopcion"
FOR EACH ROW
EXECUTE FUNCTION trg_sync_animal_estado();

-- Validación especie/raza
CREATE OR REPLACE FUNCTION trg_check_raza_especie()
RETURNS trigger
LANGUAGE plpgsql
AS $$
DECLARE
  v_nombre_especie TEXT;
BEGIN
  SELECT nombre_AnimalEspecie
    INTO v_nombre_especie
  FROM "AnimalEspecie"
  WHERE id_AnimalEspecie = NEW.id_AnimalEspecie;

  IF v_nombre_especie IS NULL THEN
    RAISE EXCEPTION 'AnimalEspecie inexistente: %', NEW.id_AnimalEspecie;
  END IF;

  IF v_nombre_especie = 'Perro' AND NEW.id_RazaGato IS NOT NULL THEN
    RAISE EXCEPTION 'Inconsistencia especie/raza: Perro no puede tener id_RazaGato';
  END IF;

  IF v_nombre_especie = 'Gato' AND NEW.id_RazaPerro IS NOT NULL THEN
    RAISE EXCEPTION 'Inconsistencia especie/raza: Gato no puede tener id_RazaPerro';
  END IF;

  RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS tg_check_raza_especie ON "Animal";
CREATE TRIGGER tg_check_raza_especie
BEFORE INSERT OR UPDATE ON "Animal"
FOR EACH ROW
EXECUTE FUNCTION trg_check_raza_especie();

-- ======================================================
-- VISTAS ÚTILES (NO CAMBIAN DATOS)
-- ======================================================

-- Vacunas: vigencia y refuerzo (derivado del catálogo)
CREATE OR REPLACE VIEW "vw_AnimalVacunaVigencia" AS
SELECT
  av.id_Animal,
  av.id_VacunaCatalogo,
  vc.nombre_VacunaCatalogo,
  av.fecha_aplicacion,
  av.fecha_refuerzo,
  (av.fecha_aplicacion + (vc.dias_vigencia_VacunaCatalogo || ' days')::interval)::date AS fecha_vencimiento,
  (CURRENT_DATE <= (av.fecha_aplicacion + (vc.dias_vigencia_VacunaCatalogo || ' days')::interval)::date) AS vigente,
  CASE
    WHEN vc.dias_refuerzo_VacunaCatalogo IS NULL THEN NULL
    ELSE (av.fecha_aplicacion + (vc.dias_refuerzo_VacunaCatalogo || ' days')::interval)::date
  END AS fecha_sugerida_refuerzo,
  CASE
    WHEN vc.dias_refuerzo_VacunaCatalogo IS NULL THEN FALSE
    WHEN av.fecha_refuerzo IS NULL THEN TRUE
    ELSE FALSE
  END AS refuerzo_pendiente
FROM "AnimalVacuna" av
JOIN "VacunaCatalogo" vc ON vc.id_VacunaCatalogo = av.id_VacunaCatalogo;

-- Necesidades especiales (derivado: alergias/padecimientos/antecedentes)
CREATE OR REPLACE VIEW "vw_AnimalNecesidadesEspeciales" AS
SELECT
  a.id_Animal,
  a.nombre_Animal,
  (
    EXISTS (SELECT 1 FROM "AnimalAlergia" aa WHERE aa.id_Animal = a.id_Animal)
    OR EXISTS (SELECT 1 FROM "AnimalPadecimiento" ap WHERE ap.id_Animal = a.id_Animal)
    OR EXISTS (SELECT 1 FROM "AnimalAntecedente" an WHERE an.id_Animal = a.id_Animal)
  ) AS necesita_cuidados_especiales
FROM "Animal" a;

CREATE OR REPLACE VIEW "vw_RelacionMascotaAdoptanteIdoneo" AS
SELECT 
    a.id_Animal,
    a.nombre_Animal,
    t.nombre_Talla,
    p.nombre_Persona || ' ' || p.apellidos_Persona AS nombre_adoptante,
    ne.nombre_AdoptanteNivelEconomico,
    vt.nombre_ViviendaTipo,
    ad.patio_Adoptante,
    sne.necesita_cuidados_especiales,
    CASE 
        -- Regla 1: Salud y Economía (Prioridad Alta)
        WHEN sne.necesita_cuidados_especiales = TRUE AND ne.nombre_AdoptanteNivelEconomico = 'Alto' 
            THEN 'Idóneo: Cuenta con nivel económico para cubrir necesidades especiales de salud.'
        
        -- Regla 2: Espacio para Tallas Grandes
        WHEN t.nombre_Talla IN ('Grande', 'Gigante') AND ad.patio_Adoptante = TRUE 
            THEN 'Idóneo: Cuenta con patio para la talla del animal.'
            
        -- Regla 3: Tallas Chicas en Departamentos
        WHEN t.nombre_Talla = 'Chico' AND vt.nombre_ViviendaTipo = 'Departamento' 
            THEN 'Idóneo: Talla adecuada para el tipo de vivienda (Departamento).'
            
        -- Regla 4: Compatibilidad General (Nivel medio/Casa con patio)
        WHEN ad.patio_Adoptante = TRUE AND vt.nombre_ViviendaTipo = 'Casa' 
            THEN 'Idóneo: Espacio estándar compatible.'
            
        ELSE 'No compatible: No cumple con los criterios mínimos de espacio o presupuesto de salud.'
    END AS justificacion_idoneidad
FROM "Animal" a
JOIN "AnimalTalla" t ON a.id_AnimalTalla = t.id_AnimalTalla
JOIN "vw_AnimalNecesidadesEspeciales" sne ON a.id_Animal = sne.id_Animal
CROSS JOIN "Adoptante" ad
JOIN "Persona" p ON ad.id_Persona = p.id_Persona
JOIN "ViviendaTipo" vt ON ad.id_ViviendaTipo = vt.id_ViviendaTipo
JOIN "AdoptanteNivelEconomico" ne ON ad.id_AdoptanteNivelEconomico = ne.id_AdoptanteNivelEconomico
WHERE a.id_AnimalEstado = (SELECT id_AnimalEstado FROM "AnimalEstado" WHERE nombre_AnimalEstado = 'Disponible');

-- Expediente animal
CREATE OR REPLACE VIEW "vw_ExpedienteAnimalCompleto" AS
SELECT 
    a.id_Animal,
    a.nombre_Animal,
    a.clave_ruac_Animal,
    e.nombre_AnimalEspecie AS especie,
    s.nombre_AnimalSexo AS sexo,
    COALESCE(rp.nombre_RazaPerro, rg.nombre_RazaGato, 'Mestizo/Único') AS raza, -- Razas nulas = mestizo/único
    t.nombre_Talla AS talla,
    tp.nombre_AnimalTipo AS tipo,
    a.peso_Animal,
    a.edad_anios_Animal || ' años, ' || a.edad_meses_Animal || ' meses' AS edad_formateada,
    sd.nombre_Sede AS sede_actual,
    (SELECT COUNT(*) FROM "Fotografia" f WHERE f.id_Animal = a.id_Animal) AS total_fotos
FROM "Animal" a
JOIN "AnimalEspecie" e ON a.id_AnimalEspecie = e.id_AnimalEspecie
JOIN "AnimalSexo" s ON a.id_AnimalSexo = s.id_AnimalSexo
JOIN "AnimalTalla" t ON a.id_AnimalTalla = t.id_AnimalTalla
JOIN "AnimalTipo" tp ON a.id_AnimalTipo = tp.id_AnimalTipo
JOIN "Sede" sd ON a.id_Sede = sd.id_Sede
LEFT JOIN "RazaPerro" rp ON a.id_RazaPerro = rp.id_RazaPerro
LEFT JOIN "RazaGato" rg ON a.id_RazaGato = rg.id_RazaGato;

-- Control de adopciones
CREATE OR REPLACE VIEW "vw_SeguimientoProcesosActivos" AS
SELECT 
    pa.id_ProcesoAdopcion,
    ani.nombre_Animal,
    p_adoptante.nombre_Persona || ' ' || p_adoptante.apellidos_Persona AS adoptante,
    p_voluntario.nombre_Persona AS responsable_interno,
    est.nombre_ProcesoAdopcionEstado AS fase_actual,
    pa.fecha_inicio_Proceso,
    cit.fecha_hora_cita AS proxima_cita
FROM "ProcesoAdopcion" pa
JOIN "Animal" ani ON pa.id_Animal = ani.id_Animal
JOIN "Adoptante" ad ON pa.id_Adoptante = ad.id_Adoptante
JOIN "Persona" p_adoptante ON ad.id_Persona = p_adoptante.id_Persona
LEFT JOIN "Voluntario" vol ON pa.id_Voluntario = vol.id_Voluntario
LEFT JOIN "Persona" p_voluntario ON vol.id_Persona = p_voluntario.id_Persona
JOIN "ProcesoAdopcionEstado" est ON pa.id_ProcesoAdopcionEstado = est.id_ProcesoAdopcionEstado
LEFT JOIN "ProcesoAdopcionCita" cit ON pa.id_ProcesoAdopcion = cit.id_ProcesoAdopcion
WHERE pa.fecha_cierre_Proceso IS NULL;

-- Resumen Financiero
CREATE OR REPLACE VIEW "vw_EstadoCuentasAcreedores" AS
SELECT 
    acr.nombre_Comercial_Acreedor,
    acr.rfc_Acreedor,
    cpp.concepto_Deuda,
    cpp.monto_Original,
    cpp.monto_Abonado,
    cpp.saldo_Pendiente,
    cpp.fecha_Vencimiento,
    cpp.estado_Pago,
    CASE 
        WHEN cpp.fecha_Vencimiento < CURRENT_DATE AND cpp.estado_Pago = 'Pendiente' THEN 'VENCIDA'
        ELSE 'EN TIEMPO'
    END AS estatus_vencimiento
FROM "CuentaPorPagar" cpp
JOIN "Acreedor" acr ON cpp.id_Acreedor = acr.id_Acreedor;

-- Dashboard Voluntarios
CREATE OR REPLACE VIEW "vw_DashboardVoluntarios" AS
SELECT 
    v.id_Voluntario,
    p.nombre_Persona || ' ' || p.apellidos_Persona AS nombre_completo,
    vr.nombre_VoluntarioRol AS rol,
    s.nombre_Sede AS sede_actual,
    (SELECT entrada FROM "VoluntarioAsistencia" va 
     WHERE va.id_Voluntario = v.id_Voluntario AND va.salida IS NULL 
     ORDER BY entrada DESC LIMIT 1) AS ultima_entrada_activa
FROM "Voluntario" v
JOIN "Persona" p ON v.id_Persona = p.id_Persona
JOIN "VoluntarioRol" vr ON v.id_VoluntarioRol = vr.id_VoluntarioRol
LEFT JOIN "VoluntarioSedeAsignacion" vsa ON v.id_Voluntario = vsa.id_Voluntario AND vsa.fecha_fin IS NULL
LEFT JOIN "Sede" s ON vsa.id_Sede = s.id_Sede;

CREATE OR REPLACE VIEW "vw_ValidarAdoptante" AS
SELECT 
    p.id_Persona,
    p.nombre_Persona || ' ' || p.apellidos_Persona AS nombre,
    EXISTS (SELECT 1 FROM "PersonaBlacklist" pb WHERE pb.id_Persona = p.id_Persona) AS esta_en_blacklist,
    (SELECT COUNT(*) FROM "ProcesoAdopcion" pa 
     JOIN "Adoptante" ad ON pa.id_Adoptante = ad.id_Adoptante 
     WHERE ad.id_Persona = p.id_Persona AND pa.fecha_cierre_Proceso IS NULL) AS procesos_activos_totales
FROM "Persona" p;

-- ======================================================
-- Procedimientos almacenados (SP)
-- ======================================================

-- Registrar rescate completo (dirección + reporte + animal)
CREATE OR REPLACE PROCEDURE sp_registrar_rescate_completo(
    -- Datos Dirección
    p_estado VARCHAR, p_municipio VARCHAR, p_calle VARCHAR,
    -- Datos Animal
    p_nombre VARCHAR, p_especie_id INT, p_sexo_id INT, p_talla_id INT, 
    p_tipo_id INT, p_funcion_id INT, p_medio_id INT, p_patron_id INT,
    p_color_ojos_id INT, p_color_pri_id INT, p_caracter_id INT,
    p_peso NUMERIC, p_anios INT, p_meses INT, p_sede_id INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_id_dir INT;
    v_id_reporte INT;
    v_id_estado_disp INT;
BEGIN
    -- 1. Obtener ID de estado 'Disponible'
    SELECT id_AnimalEstado INTO v_id_estado_disp FROM "AnimalEstado" WHERE nombre_AnimalEstado = 'Disponible';

    -- 2. Insertar Dirección
    INSERT INTO "Direccion" (estado_Direccion, municipio_Direccion, calle_Direccion)
    VALUES (p_estado, p_municipio, p_calle) RETURNING id_Direccion INTO v_id_dir;

    -- 3. Crear Reporte Automático
    INSERT INTO "ReporteAnimal" (id_Direccion, id_ColorPrincipal, id_ColorOjos, fecha_ReporteAnimal)
    VALUES (v_id_dir, p_color_pri_id, p_color_ojos_id, now()) RETURNING id_ReporteAnimal INTO v_id_reporte;

    -- 4. Crear Animal vinculado al reporte
    INSERT INTO "Animal" (
        nombre_Animal, id_AnimalEspecie, id_AnimalSexo, id_AnimalTalla, id_AnimalTipo,
        id_AnimalFuncion, id_MedioLlegada, id_PatronPelaje, id_ColorOjos, id_ColorPrincipal,
        id_AnimalCaracter, id_AnimalEstado, peso_Animal, edad_anios_Animal, edad_meses_Animal,
        id_Sede, id_ReporteAnimal
    ) VALUES (
        p_nombre, p_especie_id, p_sexo_id, p_talla_id, p_tipo_id,
        p_funcion_id, p_medio_id, p_patron_id, p_color_ojos_id, p_color_pri_id,
        p_caracter_id, v_id_estado_disp, p_peso, p_anios, p_meses,
        p_sede_id, v_id_reporte
    );
END;
$$;